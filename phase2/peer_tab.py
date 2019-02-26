from PyQt5.QtWidgets import *

class peer_tab(QWidget):
    def __init__(self):
        super().__init__()
        
        # specify layout (horizontal* or vertical)
        self.main_layout = QVBoxLayout()
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
        self.main_layout.addLayout(self.browse_layout)

        # PORT
        self.port_textBox = QLineEdit()
        self.port_textBox.setPlaceholderText("Port ")
        # USERNAME
        self.username_textBox = QLineEdit()
        self.username_textBox.setPlaceholderText("Username ")
        # ADDRESS
        self.address_textBox = QLineEdit()
        self.address_textBox.setPlaceholderText("Address ")
        # PASSWORD
        self.pass_textBox = QLineEdit()
        self.pass_textBox.setPlaceholderText("Password ")
        # addding abvoe widget to layout
        self.main_layout.addWidget(self.port_textBox)
        self.main_layout.addWidget(self.username_textBox)
        self.main_layout.addWidget(self.address_textBox)
        self.main_layout.addWidget(self.pass_textBox)
        
        # self.send_btn.setProperty('background-position', left)
        self.send_btn = QPushButton("Send")
        self.send_btn.setMaximumWidth(100)
        self.send_btn.clicked.connect(self.send_files)


        self.main_layout.addWidget(self.send_btn)
        self.setLayout(self.main_layout)

    #  when browse button is clicked
    # open the dialog box and return the file path to browse_textBox
    # prededined function from internet
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

    #  function to be initiated when send button is clicked
    #  file location from textBox can be extracted by  ----> self.browse_textBox.text()
    #  similarly >>>   self.port_textBox.text()      -----   self.port_textBox.text()   ----- self.address_textBox.text()
    def send_files(self):
        import subprocess
        cmd = "ssh -p %s %s %s@%s" % (self.port_textBox.text(), self.browse_textBox.text(),  self.port_textBox.text(), self.address_textBox.text())
        try:
            returned_output = subprocess.check_output(cmd)
            print('>>>>', returned_output.decode("utf-8"))
        except subprocess.CalledProcessError:
            print("error11")            
        except:
            print("error12")
        try:
            returned_output = subprocess.check_output(self.pass_textBox.text())
            print('>>>>', returned_output.decode("utf-8"))
        except subprocess.CalledProcessError:
            print("error21")            
        except:
            print("error22")
        
        # print(opera.scp_query())
        # cmd = "scp -P %s %s u0_a191@%s:~/ " % (self.ip_add_port_text, self.filenames, self.ip_add_text)
        # os.system(cmd)
