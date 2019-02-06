from PyQt5.QtWidgets import QFileDialog, QListView, QTreeView, QAbstractItemView
from Views.designer.classify_page import Ui_ClassifyPage
from Views.designer.info_page import Ui_InfoPage
from Views.designer.main_window import Ui_MainWindow
from utils import images_in_dir


class MainWindowUIClass(Ui_MainWindow):
    def __init__(self):
        '''Initialize the super class
        '''
        super().__init__()

    def setupUi(self, MW):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi(MW)


class InfoPageUIClass(Ui_InfoPage):
    def __init__(self):
        '''Initialize the super class
        '''
        super().__init__()
        self.layout = BorderLayout()

    def setupUi(self, MW):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi(MW)



class ClassifyPageUIClass(Ui_ClassifyPage):
    def __init__(self):
        '''Initialize the super class
        '''
        super().__init__()

    def setupUi(self, MW):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi(MW)

    def debugPrint( self, msg ):
        '''Print the message in the text edit at the bottom of the
        horizontal splitter.
        '''
        self.listWidget.addItem(msg)


    def pickDatasetSlot(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        dlg.setOption(QFileDialog.DontUseNativeDialog)
        lis = dlg.findChild(QListView, "listView")
        tree = dlg.findChild(QTreeView, "treeView")
        if tree:
            tree.setSelectionMode(QAbstractItemView.MultiSelection)
        if lis:
            lis.setSelectionMode(QAbstractItemView.MultiSelection)
        if dlg.exec():
            data_path = dlg.selectedFiles()
            input = images_in_dir(data_path)
            self.listWidget.addItems(input)
        else:
            print("No data path was given")

    def classifySlot(self):
        self.debugPrint("classify")

    def cancelSlot(self):
        self.debugPrint("cancel")

