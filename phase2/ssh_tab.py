from PyQt5.QtWidgets import *

class ssh_tab(QWidget):
    def __init__(self):
        super().__init__()
        
        # main layout is vertical
        self.main_layout = QVBoxLayout()
        # LABEL
        self.label = QLabel()
        self.label.setText("Enter commands")
        # TEXTBOX where commands are entered
        self.cmd_text = QLineEdit()
        self.cmd_text.returnPressed.connect(self.display)
        # TEXTAERA where results are shown
        self.text_area = QPlainTextEdit()
        self.text_area.setReadOnly(True)

        # addign widgets to layout
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.cmd_text)
        self.main_layout.addWidget(self.text_area)
        self.setLayout(self.main_layout)

    # when the enter is pressed on textBox
    # this function is initiated
    def display(self):
        import subprocess
        # get commands from cmd_text
        self.text_area.appendPlainText('>>>> ' + self.cmd_text.text())
        try:
            # run command on shell
        	returned_output = subprocess.check_output(self.cmd_text.text())
        	print('>>>>', returned_output.decode("utf-8"))
            # print and display output on shell and text_area
        	self.text_area.appendPlainText(returned_output.decode("utf-8"))
        except:
            # if any error occured
        	print('something went wrong')