import platform

import PyQt5.QtCore
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class WebBrowser(QMainWindow):


    def __init__(self):

        def useragent(self=None):
            # Fetch platform and device information
            platform_info = platform.platform()
            device_info = platform.uname().machine

            # Create the user-agent string including PyQt5 information
            user_agent = f"PhantomCrawler/1.1 (PyQt5; {platform_info}; {device_info})"

            # Set the modified user-agent for the web browser
            self.browser.page().profile().setHttpUserAgent(user_agent)


        self.window = QWidget()
        self.window.setWindowTitle("Phantom Crawler")
#        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("GO")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.inspect_btn = QPushButton("🔧")
        self.inspect_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.inspect_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.inspect_btn.clicked.connect(lambda: self.navigate("view-source:" + self.url_bar.toPlainText()))


        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(PyQt5.QtCore.QUrl("https://i.ibb.co/B6yjh11/logo.png"))

        self.window.setLayout(self.layout)
        self.window.show()

        useragent(self)


    def navigate(self, url):

        if not url.startswith("view-source:"):
            if not url.startswith("http"):
                url = "http://" + url
                self.url_bar.setText(url)
        self.browser.setUrl(PyQt5.QtCore.QUrl(url))
        



app = QApplication([])
window = WebBrowser()
app.exec_()