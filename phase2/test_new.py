import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from broadcast_tab import broadcast_tab  
from ssh_tab import ssh_tab
from peer_tab import peer_tab
from find_tab import find_tab
from settings_tab import settings_tab


# create application interface
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

    # assistent app application -- eg: applet
    def Assistant(self):
        self.mainLayout = QVBoxLayout()

        self.tabs = QTabWidget()

        # un-necessary styling applied :P
        self.tabs.setStyleSheet("QTabBar::tab:disabled {"+\
                        "width: 10px;"+\
                        "color: transparent;"+\
                        "background: transparent;}")



        self.tabs.addTab(broadcast_tab(opera), "Broadcast")
        
        # self.peer_tab = QWidget(parent=None)
        # self.tabs.addTab(self.peer_tab, "P2P")
        
        self.tabs.addTab(peer_tab(), "P2P")
        self.tabs.addTab(ssh_tab(), "CMD")
        self.tabs.addTab(find_tab(), "Find")

        self.emptySpace = QWidget()
        self.tabs.addTab(self.emptySpace,"ES")
        self.tabs.setTabEnabled(4,False)
                
        self.settings_tab = QWidget()
        self.tabs.addTab(settings_tab(), "Settings")

        self.mainLayout.addWidget(self.tabs)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())
