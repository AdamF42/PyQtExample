from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QSize, QRect, QPoint
from PyQt5.QtWidgets import (QComboBox, QStackedWidget, QVBoxLayout, QWidget, QTabBar, QStylePainter, QStyleOptionTab,
                             QStyle, QTabWidget, QProxyStyle)


class PyMultiPageWidget(QWidget):
    currentIndexChanged = pyqtSignal(int)
    pageTitleChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        super(PyMultiPageWidget, self).__init__(parent)

        self.comboBox = QComboBox()
        self.comboBox.setObjectName('__qt__passive_comboBox')
        self.stackWidget = QStackedWidget()
        self.comboBox.activated.connect(self.setCurrentIndex)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.stackWidget)
        self.setLayout(self.layout)

    def sizeHint(self):
        return QSize(200, 150)

    def count(self):
        return self.stackWidget.count()

    def widget(self, index):
        return self.stackWidget.widget(index)

    @pyqtSlot(QWidget)
    def addPage(self, page):
        self.insertPage(self.count(), page)

    @pyqtSlot(int, QWidget)
    def insertPage(self, index, page):
        page.setParent(self.stackWidget)
        self.stackWidget.insertWidget(index, page)
        title = page.windowTitle()
        if title == "":
            title = "Page %d" % (self.comboBox.count() + 1)
            page.setWindowTitle(title)
        self.comboBox.insertItem(index, title)

    @pyqtSlot(int)
    def removePage(self, index):
        widget = self.stackWidget.widget(index)
        self.stackWidget.removeWidget(widget)
        self.comboBox.removeItem(index)

    def getPageTitle(self):
        cw = self.stackWidget.currentWidget()
        return cw.windowTitle() if cw is not None else ''

    @pyqtSlot(str)
    def setPageTitle(self, newTitle):
        cw = self.stackWidget.currentWidget()
        if cw is not None:
            self.comboBox.setItemText(self.getCurrentIndex(), newTitle)
            cw.setWindowTitle(newTitle)
            self.pageTitleChanged.emit(newTitle)

    def getCurrentIndex(self):
        return self.stackWidget.currentIndex()

    @pyqtSlot(int)
    def setCurrentIndex(self, index):
        if index != self.getCurrentIndex():
            self.stackWidget.setCurrentIndex(index)
            self.comboBox.setCurrentIndex(index)
            self.currentIndexChanged.emit(index)

    pageTitle = pyqtProperty(str, fget=getPageTitle, fset=setPageTitle, stored=False)
    currentIndex = pyqtProperty(int, fget=getCurrentIndex, fset=setCurrentIndex)


class VerticalTabBarWidget(QTabBar):
    def tabSizeHint(self, index):
        s = QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QStylePainter(self)
        opt = QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QRect(QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QStyle.CE_TabBarTabLabel, opt);
            painter.restore()


class PyVerticalTabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(VerticalTabBarWidget(self))
        self.setTabPosition(QTabWidget.West)

class ProxyStyle(QProxyStyle):
    def drawControl(self, element, opt, painter, widget):
        if element == QStyle.CE_TabBarTabLabel:
            ic = self.pixelMetric(QStyle.PM_TabBarIconSize)
            r = QRect(opt.rect)
            w =  0 if opt.icon.isNull() else opt.rect.width() + self.pixelMetric(QStyle.PM_TabBarIconSize)
            r.setHeight(opt.fontMetrics.width(opt.text) + w)
            r.moveBottom(opt.rect.bottom())
            opt.rect = r
        QProxyStyle.drawControl(self, element, opt, painter, widget)