import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from broadcast_tab import broadcast_tab  

class ssh_tab(QWidget):
    def __init__(self):
        super().__init__()
        
        self.tab2_layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setText("SSH window")
        self.cmd_text = QLineEdit()
        self.cmd_text.returnPressed.connect(self.display)
        self.text_area = QPlainTextEdit()
        self.text_area.setReadOnly(True)

        self.tab2_layout.addWidget(self.label)
        self.tab2_layout.addWidget(self.cmd_text)
        self.tab2_layout.addWidget(self.text_area)
        self.setLayout(self.tab2_layout)

    def display(self):
        import subprocess
        self.text_area.appendPlainText('>>>> ' + self.cmd_text.text())
        returned_output = subprocess.check_output(self.cmd_text.text())
        print('>>>>', returned_output.decode("utf-8"))
        self.text_area.appendPlainText(returned_output.decode("utf-8"))
        


'''

class broadcast_tab(QWidget):
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

        # self.send_layout = QHBoxLayout()
        # self.send_layout.addStretch()
        # self.send_btn.setProperty('background-position', left)
        self.send_btn = QPushButton("Send")
        self.send_btn.setMaximumWidth(100)
        self.send_btn.clicked.connect(self.send_files)


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
            self.filenames = dlg.selectedFiles()
            self.browse_textBox.setText(",".join(self.filenames))
            print(self.filenames[0])
            return self.filenames

    def send_files(self):
        print(opera.scp_query())
        # cmd = "scp -P %s %s u0_a191@%s:~/ " % (self.ip_add_port_text, self.filenames, self.ip_add_text)
        # os.system(cmd)

'''

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 150, 550, 200)
        self.setWindowTitle("Virtual Lab Assistant")
        self.platform()
        # plat = self.platform() 
        # if plat == 1:
        #     import win as opera
        #     global opera
        # elif plat == -1:
        #     import lin as opera
        #     global opera
        # else:
        #     print("OS not identified")
        self.Assistant()

    def platform(self):
        import platform
        if platform.system() == 'Windows':
            print("Windows")
            import win as opera
            global opera
        elif platform.system() == 'Linux':
            print("linux")
            import win as opera
            global opera
        else:
            print("error loading os")
            return 0

    # def platform(self):
    #     import platform
    #     if platform.system() == 'Windows':
    #         print("Windows")
    #         return 1
    #     elif platform.system() == 'Linux':
    #         print("linux")
    #         return -1
    #     else:
    #         return 0


    def Assistant(self):
        self.mainLayout = QVBoxLayout()

        self.tabs = QTabWidget()

        self.tabs.addTab(broadcast_tab(opera), "Broadcast")
        
        self.peer_tab = QWidget(parent=None)
        self.tabs.addTab(self.peer_tab, "P2P")
        
        self.tabs.addTab(ssh_tab(), "SSH")


        self.mainLayout.addWidget(self.tabs)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())
