from PyQt5.QtWidgets import *


class broadcast_tab(QWidget):
    def __init__(self, op):
        super().__init__()
        global opera
        opera = op
        print(opera)
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

