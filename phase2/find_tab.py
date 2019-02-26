from PyQt5.QtWidgets import *

class find_tab(QWidget):
    def __init__(self):
        super().__init__()
        
        # specifying the main layout is vertical layout
        self.main_layout = QVBoxLayout()
        
        # find label created and added to layout
        self.label = QLabel()
        self.label.setText("File to find: ")
        self.main_layout.addWidget(self.label)
        
        #  horizontal layout contail find_textbox , find_button
        self.find_layout = QHBoxLayout()
        self.find_textBox = QLineEdit()
        self.find_button = QPushButton("Find")
        self.find_button.clicked.connect(self.find)

        # widgets added to layout
        self.find_layout.addWidget(self.find_textBox)
        self.find_layout.addWidget(self.find_button)
        self.main_layout.addLayout(self.find_layout)        

        # creating the text_area (not editable by user) and add to main_layout
        self.text_area = QPlainTextEdit()
        self.text_area.setReadOnly(True)

        self.main_layout.addWidget(self.text_area)
        self.setLayout(self.main_layout)

    # function initiated when user click the find button
    def find(self):
        # write the backend code for find
        # where the file to find can be accessed by the  ----> "file_name = self.textBox.text()"
        # expected output can be printed to the textArea ----> "self.text_area.appendPlainText("<----output---->")"  or 
        # "self.text_area.setPlainText(const QString &text)"
        pass
        
