import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import *


class transfer_tab(QWidget):
    def __init__(self):
        super().__init__()
        # specify layout (horizontal* or vertical)
        self.tab1_layout = QVBoxLayout()

        # radio buttons and adding it to sub-layout (horizontal)
        self.radio_layout = QHBoxLayout()
        self.file_radio = QRadioButton("File")
        self.dir_radio = QRadioButton("Directory")
        self.file_radio.setChecked(True)
        self.radio_layout.addWidget(self.file_radio)
        self.radio_layout.addWidget(self.dir_radio)

        self.browse_layout = QHBoxLayout()
        # file label
        self.file_label = QLabel()
        self.file_label.setText("File: ")
        # browse textBox
        self.browse_textBox = QLineEdit(self)
        # browse button
        self.browse_btn = QPushButton("Browse")
        # event to be triggered
        self.browse_btn.clicked.connect(self.openDialog)
        # adding the above widget to the layout (tab1)
        self.browse_layout.addWidget(self.file_label)
        self.browse_layout.addWidget(self.browse_textBox)
        self.browse_layout.addWidget(self.browse_btn)

        self.tab1_layout.addLayout(self.radio_layout)
        self.tab1_layout.addLayout(self.browse_layout)

        self.send_btn = QPushButton("Send")
        self.send_btn.setMaximumWidth(100)
        self.tab1_layout.addWidget(self.send_btn)

        self.setLayout(self.tab1_layout)

    # open the dialog box and return the file
    def openDialog(self):
        dlg = QFileDialog()
        if self.dir_radio.isChecked():
            dlg.setFileMode(QFileDialog.Directory)
        else:
            dlg.setFileMode(QFileDialog.ExistingFiles)
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.browse_textBox.setText(",".join(filenames))
            print(filenames)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 150, 550, 200)
        self.setWindowTitle("Virtual Lab Assistant")
        self.Assistant()

    def Assistant(self):
        self.mainLayout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tab2 = QWidget(parent=None)

        self.tabs.addTab(transfer_tab(), "Transfer")
        self.tabs.addTab(self.tab2, "Tab 2")

        self.mainLayout.addWidget(self.tabs)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())