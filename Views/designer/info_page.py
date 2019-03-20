# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InfoPage(object):
    def setupUi(self, InfoPage):
        InfoPage.setObjectName("InfoPage")
        InfoPage.resize(500, 480)
        self.textBrowser = QtWidgets.QTextBrowser(InfoPage)
        self.textBrowser.setGeometry(QtCore.QRect(50, 45, 420, 360))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(InfoPage)
        QtCore.QMetaObject.connectSlotsByName(InfoPage)

    def retranslateUi(self, InfoPage):
        _translate = QtCore.QCoreApplication.translate
        InfoPage.setWindowTitle(_translate("InfoPage", "Form"))
        self.textBrowser.setHtml(_translate("InfoPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a name=\"lipsum\"></a><span style=\" font-family:\'Open Sans,Arial,sans-serif\'; font-size:12pt; color:#000000;\">L</span><span style=\" font-family:\'Open Sans,Arial,sans-serif\'; font-size:12pt; color:#000000;\">orem ipsum dolor sit amet, consectetur adipiscing elit. Fusce egestas, ex dictum mattis viverra, mauris ex placerat tellus, quis euismod elit diam mattis urna. Vivamus posuere consectetur tortor vitae lobortis. Ut suscipit a turpis ultricies dictum. Suspendisse luctus nisi a libero aliquet, ut dictum ligula vulputate. Suspendisse nec volutpat tortor. Praesent iaculis nibh quam, vel auctor odio ullamcorper at. Quisque ullamcorper, lectus auctor elementum bibendum, est erat suscipit enim, ac consequat elit mi a magna.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"><br /></span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoPage = QtWidgets.QWidget()
    ui = Ui_InfoPage()
    ui.setupUi(InfoPage)
    InfoPage.show()
    sys.exit(app.exec_())

