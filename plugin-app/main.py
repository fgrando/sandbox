#!/bin/python3

from plugins import Base

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QTreeWidget, QGroupBox, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QHeaderView, QTabWidget, QHBoxLayout, QMenu, QTextEdit, QApplication, QComboBox, QMainWindow, QPushButton, QFileDialog, QGridLayout
from PyQt5.QtGui import QTextCharFormat, QSyntaxHighlighter, QColor, QTextCursor

from collections import OrderedDict


import sys
data = '''
<!-- #######  THIS IS A COMMENT - Visible only in the source editor #########-->
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
<h2>Welcome To The Best Online HTML Web Editor!</h2>
<p style="font-size: 1.5em;">You can <strong style="background-color: #317399; padding: 0 5px; color: #fff;">type your text</strong> directly in the editor or paste it from a Word Doc, PDF, Excel etc.</p>
<p style="font-size: 1.5em;">The <strong>visual editor</strong> on the right and the <strong>source editor</strong> on the left are linked together and the changes are reflected in the other one as you type! <img src="https://html5-editor.net/images/smiley.png" alt="smiley" /></p>
<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Magazzini Alimentari Riuniti</td>
    <td>Giovanni Rovelli</td>
    <td>Italy</td>
  </tr>
</table>


<table>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$80</td>
  </tr>
    <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$80</td>
  </tr>
<tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$80</td>
  </tr>
</table>

<img src="pic.png" alt="Image caption">
<p>This is a table you can experiment with.</p>
'''
import re

class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        QSyntaxHighlighter.__init__(self, parent)

        self._mappings = {}

    def search_now(self, pattern):
        fmt = QTextCharFormat()
        fmt.setBackground(QColor("yellow"))
        self._mappings.clear()
        self._mappings[pattern] = fmt

    def highlightBlock(self, text):
        for pattern, format in self._mappings.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, format)

class DocView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout()

        top = QHBoxLayout(self)
        self.line_doc = QLineEdit("12345")
        self.line_bl = QLineEdit("baselineXYZ")
        top.addWidget(self.line_doc)
        top.addWidget(self.line_bl)

        self.line_search = QLineEdit()
        self.line_search.setPlaceholderText("search...")
        self.line_search.textEdited.connect(self.on_search)

        self.text_view = QTextEdit()
        self.text_view .setHtml(data*1000)
        self.text_view.setReadOnly(True)

        self.layout.addLayout(top)
        self.layout.addWidget(self.line_search)
        self.layout.addWidget(self.text_view)

        self.highlighter = Highlighter(self.text_view.document())


    def on_search(self, text):
        print("search", text)
        self.text_view.find(text)
        self.highlighter.search_now(text)

    def keyPressEvent(self, e):
        print("event", e)
        if e.key()  == QtCore.Qt.Key_Return :
            print(' return')
            print(self.text_view.pos())
            text = self.line_search.text()
            self.text_view.find(text)
#            self.highlighter.search_now(text)

        elif e.key() == QtCore.Qt.Key_Enter :
            print(' enter')



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
        self.tabs.addTab(DocView(self), "doc bl")


        self.tree_editor = QTreeWidget()
        self.tree_editor.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.btn_save = QPushButton("&Save File")



        layout = QVBoxLayout()
        #layout.addWidget(self.btn_load)
        #layout.addWidget(self.lbl_path)
        #layout.addWidget(self.tree_editor)
        #layout.addWidget(self.btn_save)
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
