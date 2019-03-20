# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classify_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot, QObject


class Ui_ClassifyPage(QObject):
    def setupUi(self, ClassifyPage):
        ClassifyPage.setObjectName("ClassifyPage")
        ClassifyPage.resize(500, 480)
        self.widget = QtWidgets.QWidget(ClassifyPage)
        self.widget.setGeometry(QtCore.QRect(30, 22, 450, 401))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.getFileGroupBox = QtWidgets.QGroupBox(self.widget)
        self.getFileGroupBox.setObjectName("getFileGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.getFileGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.getFileGroupBox)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.browsePushbutton = QtWidgets.QPushButton(self.getFileGroupBox)
        self.browsePushbutton.setEnabled(True)
        self.browsePushbutton.setObjectName("browsePushbutton")
        self.horizontalLayout.addWidget(self.browsePushbutton, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.getFileGroupBox)
        spacerItem = QtWidgets.QSpacerItem(448, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancelPushButton = QtWidgets.QPushButton(self.widget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_2.addWidget(self.cancelPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(193, 27, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.classifyPushButton = QtWidgets.QPushButton(self.widget)
        self.classifyPushButton.setObjectName("classifyPushButton")
        self.horizontalLayout_2.addWidget(self.classifyPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ClassifyPage)
        self.browsePushbutton.clicked.connect(self.pickDatasetSlot)
        self.classifyPushButton.clicked.connect(self.classifySlot)
        self.cancelPushButton.clicked.connect(self.cancelSlot)
        QtCore.QMetaObject.connectSlotsByName(ClassifyPage)

    def retranslateUi(self, ClassifyPage):
        _translate = QtCore.QCoreApplication.translate
        ClassifyPage.setWindowTitle(_translate("ClassifyPage", "Form"))
        self.getFileGroupBox.setTitle(_translate("ClassifyPage", "Select a file or folder to classify"))
        self.browsePushbutton.setText(_translate("ClassifyPage", "Browse"))
        self.cancelPushButton.setText(_translate("ClassifyPage", "Cancel"))
        self.classifyPushButton.setText(_translate("ClassifyPage", "Classify"))

    @pyqtSlot( )
    def pickDatasetSlot(self):
        pass

    @pyqtSlot( )
    def classifySlot(self):
        pass

    @pyqtSlot( )
    def cancelSlot(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClassifyPage = QtWidgets.QWidget()
    ui = Ui_ClassifyPage()
    ui.setupUi(ClassifyPage)
    ClassifyPage.show()
    sys.exit(app.exec_())

