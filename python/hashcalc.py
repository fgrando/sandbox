#!/bin/python3

import os
import sys
import signal
import hashlib
import zlib

# pip install pyqt5

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QTableWidget, QFileDialog, QTableWidgetItem, QLabel, QSizePolicy


signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        title = os.path.basename(sys.argv[0])
        self.setWindowTitle(title)
        self.resize(500, 180)
        self.setAcceptDrops(True)

        # Add available HASH algorithms
        self.algos = {
            'md5':    self.calculateMD5,
            'sha256': self.calculateSHA256,
            'CRC-32': self.calculateCRC32,
        }


        self.tableWidget = QTableWidget()
        self.tableWidget.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.tableWidget.setRowCount(1 + len(self.algos.keys())) # header + algorithms
        self.tableWidget.setColumnCount(2)
        
        msg = "drag and drop a file to calculate" 
        self.tableWidget.setItem(0,0, QTableWidgetItem("File"))
        self.tableWidget.setItem(0,1, QTableWidgetItem(msg))
        row = 1
        for algo in self.algos.keys():
            self.tableWidget.setItem(row,0, QTableWidgetItem(algo))
            self.tableWidget.setItem(row,1, QTableWidgetItem(msg))
            row += 1
        self.tableWidget.move(0,0)
        self.tableWidget.resizeColumnsToContents()
       
        self.setCentralWidget(self.tableWidget)


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()


    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        file = files[0] # use only first file
        self.tableWidget.setItem(0,1, QTableWidgetItem(file))
        # skip header row
        row = 1
        for algo in self.algos.keys():
            result = self.algos[algo](file)
            self.tableWidget.setItem(row,0, QTableWidgetItem(algo))
            self.tableWidget.setItem(row,1, QTableWidgetItem(result))
            row += 1
        self.tableWidget.move(0,0)
        self.tableWidget.resizeColumnsToContents()

        # create a dump from the current table contents
        dump = ''
        for row in range(self.tableWidget.rowCount()):
            dump += f'{self.tableWidget.item(row, 0).text()}\t{self.tableWidget.item(row, 1).text()}\n'
        self.saveFileDialog(dump, f'{file}.txt')


    def calculateMD5(self, filename):
        md5 = ''
        with open(filename, 'rb') as file_to_check:
            data = file_to_check.read()
            md5 = hashlib.md5(data).hexdigest()
        return md5

    def calculateSHA256(self, filename):
        sha256 = ''
        with open(filename, "rb") as f:
            file_bytes = f.read()
            sha256 = hashlib.sha256(file_bytes).hexdigest()
        return sha256

    def calculateCRC32(self, filename, chunksize=65536):
        with open(filename, "rb") as f:
            checksum = 0
            while (chunk := f.read(chunksize)):
                checksum = zlib.crc32(chunk, checksum)
        return format(checksum & 0xFFFFFFFF, '08x')

    def saveFileDialog(self, text, file):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self,"Save calculated results to file?",file,"All Files (*);;Text Files (*.txt)", options=options)
        if filename:
            with open(filename, 'wt') as output:
                output.write(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec_())
