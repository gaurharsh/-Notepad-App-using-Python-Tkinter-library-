import sys
from PyQt5.QtCore import QUrl 
from PyQt5.Qtwidgets import QApplication

from PyQt5.QtWebEngineWidgets import QWebEngineView


app =  QApplication(sys.argv)

view = QWebEngineView()

view.load(Qurl("https://www.google.com")) 
view.show()

sys.exit(app.exec_())