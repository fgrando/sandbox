#!/bin/python3

from plugins import Base

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QTreeWidget, QGroupBox, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QHeaderView, QTabWidget, QHBoxLayout, QMenu, QTextEdit, QApplication, QComboBox, QMainWindow, QPushButton, QFileDialog, QGridLayout
from PyQt5.QtGui import QTextCharFormat, QSyntaxHighlighter, QColor, QTextCursor

from collections import OrderedDict


import sys

import re
from record import *
from recordui import *



class ohdh(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = {}

        # load plugins
        for p in Base.plugins:
            inst = p()
            inst.start()


        self.menu = QMenu(self)
        self.menu.setEnabled(True)
        action_add = self.menu.addAction("Select Left")
        action_delete = self.menu.addAction("Compare")

        self.lbl_path = QLabel("root path")
        self.btn_load = QPushButton("Show document")

        self.tabs = QTabWidget()
        data = Record()
        self.tabs.addTab(RecordUI(data), 'new-bl233')


        self.tree_editor = QTreeWidget()
        self.tree_editor.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.btn_save = QPushButton("&Save File")



        layout = QVBoxLayout()
        layout.addWidget(self.tabs)


        main = QWidget(self)
        main.setLayout(layout)
        self.setCentralWidget(main)

        self.setWindowTitle("My App")
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)

    def contextMenuEvent(self, event):
        self.menu.exec_(event.globalPos())







if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ohdh()
    window.show()

    app.exec()
