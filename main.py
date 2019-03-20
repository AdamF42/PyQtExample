from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow)
from Views.Pages import ClassifyPageUIClass, MainWindowUIClass, InfoPageUIClass
from Widgets.CustomWidgets import PyVerticalTabWidget, ProxyStyle
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

    InfoPage = QWidget()
    ui_info = InfoPageUIClass()
    ui_info.setupUi(InfoPage)

    ClassifyPage = QWidget()
    ui_classify = ClassifyPageUIClass()
    ui_classify.setupUi(ClassifyPage)

    QApplication.setStyle(ProxyStyle())
    tabsSubPage = PyVerticalTabWidget()
    tabsSubPage.addTab(InfoPage, QIcon("zoom.png"), "Info")
    tabsSubPage.addTab(ClassifyPage, QIcon("zoom.png"), "Classify")
    tabsSubPage.addTab(QWidget(), QIcon("zoom.png"), "Train")


    MainWindow = QMainWindow()
    ui_mainwindow = MainWindowUIClass()
    ui_mainwindow.setupUi(MainWindow)
    MainWindow.setCentralWidget(tabsSubPage)

    MainWindow.show()

    sys.exit(app.exec_())