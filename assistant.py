import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import *

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 150, 650, 350)
        self.setWindowTitle("Hello")
        self.Assistant()

    def Assistant(self):
        self.layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tab1 = QWidget(parent=None)
        self.tab2 = QWidget(parent=None)

        # self.fileLabel = QFileDialog()
        self.tabs.addTab(self.tab1, "Transfer")
        self.tabs.addTab(self.tab2, "Tab 2")

        self.tab1.layout = QHBoxLayout()

        self.browse_textBox = QLineEdit(self)
        self.browse_btn = QPushButton("Browse")
        self.browse_btn.clicked.connect(self.openDialog)

        self.tab1.layout.addWidget(self.browse_textBox, stretch=0)
        self.tab1.layout.addWidget(self.browse_btn, stretch=0)

        # self.tab1.layout.addWidget(self.fileLabel)
        self.tab1.setLayout(self.tab1.layout)

        self.layout.addWidget(self.tabs)

        self.setLayout(self.layout)

    def openDialog(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.browse_textBox.setText(str(filenames))
            print(filenames)
            # f = open(filenames[0], 'r')
            #
            # with f:
            #     data = f.read()
            #     self.contents.setText(data)

        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # fileName, _ = QFileDialog.getOpenFileName(self, "", "", "All Files (*);;Python Files (*.py)", options=options)
        # if fileName:
        #     print(fileName)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())