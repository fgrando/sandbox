from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QGroupBox, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QHeaderView, QTabWidget, QHBoxLayout, QMenu, QCheckBox, QTableWidgetItem, QListWidget, QListWidgetItem, QTableWidget, QTextEdit, QApplication, QComboBox, QMainWindow, QPushButton, QFileDialog, QGridLayout
from PyQt5.QtGui import QTextCharFormat, QSyntaxHighlighter, QColor, QTextCursor
import json
import os

VIEW_FILE_EXT='.bnv'

class RecordUI(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data

        layVer = QVBoxLayout()
        self.setLayout(layVer)


        grid = QGridLayout()

        self.group_view = QGroupBox("View")
        group_layout = QVBoxLayout()

        group_layout.addWidget(QLabel("doc:"))
        group_layout.addWidget(QLineEdit("12341324"))
        group_layout.addWidget(QLabel("baseline:"))
        group_layout.addWidget(QLineEdit("BL_12341234"))

        btn_load = QPushButton("Load settings")
        btn_load.clicked.connect(self.on_load_view)
        group_layout.addWidget(btn_load)

        self.list_display_cols = QListWidget()
        self.list_display_cols.itemChanged.connect(self.on_view_item_changed)
        group_layout.addWidget(self.list_display_cols)

        btn_save = QPushButton("Save view")
        btn_save.clicked.connect(self.on_save_view)
        group_layout.addWidget(btn_save)

        self.list_display_cols.setDragDropMode(QAbstractItemView.InternalMove)
        self.list_display_cols.model().rowsMoved.connect(self.on_seq_change)

        for h in self.data.headers():
            item = QListWidgetItem(h)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            self.list_display_cols.addItem(item)

        self.group_view.setLayout(group_layout)

        self.group_filters = QGroupBox("filters")
        group_layout = QVBoxLayout()
        group_layout.addWidget(QLineEdit("search"))
        group_layout.addWidget(QLineEdit("include"))
        group_layout.addWidget(QLineEdit("exclude"))
        group_layout.addWidget(QListWidget())
        self.group_filters.setLayout(group_layout)

        self.table_contents = QTableWidget()
        self.table_contents.setRowCount(len(self.data.contents()))
        self.table_contents.setColumnCount(len(self.data.headers()))
        self.populate_table()


        grid.addWidget(self.group_view, 2,0)
        grid.addWidget(self.group_filters, 2,1)
        grid.addWidget(self.table_contents, 3, 0, 3, 2)
        layVer.addLayout(grid)

    def on_seq_change(self, *args):
        new_order = []
        for i in range(len(self.list_display_cols.count())):
            text = self.list_display_cols.item(i).text()
            new_order.append(text)
        self.data.set_headers(new_order)
        self.populate_table()

    def populate_table(self):
        self.table_contents.clear()
        self.table_contents.setHorizontalHeaderLabels(self.data.headers())
        row = 0
        for entry in self.data.contents():
            col = 0
            for hdr in self.data.headers():
                item = QTableWidgetItem(entry[hdr])
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                print(hdr, entry[hdr])
                self.table_contents.setItem(row, col, item)
                col+=1
            row+=1
        self.table_contents.horizontalHeader().setStretchLastSection(True)
        self.table_contents.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def on_save_view(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path = os.path.join(QtCore.QDir.currentPath(), 'view.bnv')
        fileName, _ = QFileDialog.getSaveFileName(self,"Save view", path, "BaseNav view (*.bnv);;All Files (*)", options=options)
        if fileName:
            print(fileName)
            if len(os.path.basename(fileName).split('.')) < 2:
                filename+=VIEW_FILE_EXT
            with open(fileName, 'w', encoding='utf-8') as fd:
                dic = {}
                dic['order'] = []
                dic['checked'] = []
                for i in range(self.list_display_cols.count()):
                    item = self.list_display_cols.item(i)
                    text = item.text()
                    dic['order'].append(text)
                    if item.checkState():
                        dic['checked'].append(text)
                json.dump(dic, fd, ensure_ascii=False, indent=4)


    def on_load_view(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Load view", "","BaseNav view (*.bnv);;All Files (*)", options=options)
        if fileName:
            with open(fileName, encoding='utf-8') as fd:
                dic = json.load(fd)
                print(dic)
                self.data.set_headers(dic['order'])

                self.list_display_cols.clear()
                for h in self.data.headers():
                    item = QListWidgetItem(h)
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    if h in dic['checked']:
                        item.setCheckState(QtCore.Qt.Checked)
                    else:
                        item.setCheckState(QtCore.Qt.Unchecked)
                    self.list_display_cols.addItem(item)

        # reload table
        self.populate_table()
        # set visible columns
        for i in range(self.list_display_cols.count()):
            self.on_view_item_changed(self.list_display_cols.item(i))


    def on_view_item_changed(self, item):
        col = self.data.headers().index(item.text())
        if item.checkState():
            self.table_contents.showColumn(col)
        else:
            self.table_contents.hideColumn(col)

    def add_view_ui(self):
        grid = QGridLayout()
        grid.addWidget(QLineEdit("view"), 0, 0)
        groupbox = QGroupBox("View panel")
        groupbox.setLayout(grid)
        return groupbox

    def add_search_ui(self):
        grid = QGridLayout()
        grid.addWidget(QLineEdit("search"), 0, 0)
        groupbox = QGroupBox("Filter panel")
        groupbox.setLayout(grid)
        return groupbox
