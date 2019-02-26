from PyQt5.QtWidgets import *

class settings_tab(QWidget):
    def __init__(self):
        super().__init__()
        
        # specify the layout is vertical
        self.main_layout = QVBoxLayout()
        self.main_layout.addStretch(1)
        
        # sub horizontal layout
        self.upd_add_layout = QHBoxLayout()
        # update label
        self.label = QLabel()
        self.label.setText("Update the address list")
        # update button
        self.update_button = QPushButton("Update")
        self.update_button.clicked.connect(self.update_address)

        # adding widget to sub-layout
        self.upd_add_layout.addWidget(self.label)
        self.upd_add_layout.addWidget(self.update_button)

        # adding sub-layout to main-layout
        self.main_layout.addLayout(self.upd_add_layout)
        self.setLayout(self.main_layout)


    # function initiated when update button is pressed
    def update_address(self):
        # created the file alive_address where output will be stored
        with open("alive_address.txt", "w") as file:
            file.write("how are you my friend")
        # write the backend code for find
        # pass
        
