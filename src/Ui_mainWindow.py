# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kilian/Dokumente/coding/M4Baker/m4baker-0.2d/m4baker/mainWindow.ui'
#
# Created: Sun Sep  5 01:39:16 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 749)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/appicon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dataTreeView = QtGui.QTreeView(self.centralwidget)
        self.dataTreeView.setEnabled(True)
        self.dataTreeView.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.dataTreeView.setProperty("showDropIndicator", False)
        self.dataTreeView.setAlternatingRowColors(True)
        self.dataTreeView.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.dataTreeView.setUniformRowHeights(True)
        self.dataTreeView.setAnimated(True)
        self.dataTreeView.setWordWrap(True)
        self.dataTreeView.setObjectName("dataTreeView")
        self.horizontalLayout_3.addWidget(self.dataTreeView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 20))
        self.menubar.setObjectName("menubar")
        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Sort = QtGui.QMenu(self.menu_Edit)
        self.menu_Sort.setObjectName("menu_Sort")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtGui.QStackedWidget(self.dockWidgetContents)
        self.stackedWidget.setObjectName("stackedWidget")
        self.infoPage = QtGui.QWidget()
        self.infoPage.setObjectName("infoPage")
        self.verticalLayout = QtGui.QVBoxLayout(self.infoPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtGui.QLabel(self.infoPage)
        self.label_13.setMinimumSize(QtCore.QSize(128, 128))
        self.label_13.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/appicon.svg"))
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_15 = QtGui.QLabel(self.infoPage)
        self.label_15.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_15.setScaledContents(False)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        spacerItem = QtGui.QSpacerItem(20, 134, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.stackedWidget.addWidget(self.infoPage)
        self.audiobookPropertiesPage = QtGui.QWidget()
        self.audiobookPropertiesPage.setObjectName("audiobookPropertiesPage")
        self.gridLayout_3 = QtGui.QGridLayout(self.audiobookPropertiesPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtGui.QLabel(self.audiobookPropertiesPage)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 2)
        self.label = QtGui.QLabel(self.audiobookPropertiesPage)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.authorEdit = QtGui.QLineEdit(self.audiobookPropertiesPage)
        self.authorEdit.setText("")
        self.authorEdit.setObjectName("authorEdit")
        self.gridLayout.addWidget(self.authorEdit, 3, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.audiobookPropertiesPage)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 2)
        self.titleEdit = QtGui.QLineEdit(self.audiobookPropertiesPage)
        self.titleEdit.setText("")
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout.addWidget(self.titleEdit, 5, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.audiobookPropertiesPage)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 2)
        self.yearEdit = QtGui.QLineEdit(self.audiobookPropertiesPage)
        self.yearEdit.setInputMask("")
        self.yearEdit.setMaxLength(4)
        self.yearEdit.setObjectName("yearEdit")
        self.gridLayout.addWidget(self.yearEdit, 7, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(217, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 2)
        self.label_7 = QtGui.QLabel(self.audiobookPropertiesPage)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 2)
        self.coverLabel = QtGui.QLabel(self.audiobookPropertiesPage)
        self.coverLabel.setMinimumSize(QtCore.QSize(128, 128))
        self.coverLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.coverLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.coverLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.coverLabel.setObjectName("coverLabel")
        self.gridLayout.addWidget(self.coverLabel, 10, 0, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 11, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.audiobookPropertiesPage)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 12, 0, 1, 2)
        self.faacEdit = QtGui.QLineEdit(self.audiobookPropertiesPage)
        self.faacEdit.setObjectName("faacEdit")
        self.gridLayout.addWidget(self.faacEdit, 13, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.audiobookPropertiesPage)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 14, 0, 1, 2)
        self.outfileEdit = QtGui.QLineEdit(self.audiobookPropertiesPage)
        self.outfileEdit.setAcceptDrops(False)
        self.outfileEdit.setReadOnly(True)
        self.outfileEdit.setObjectName("outfileEdit")
        self.gridLayout.addWidget(self.outfileEdit, 15, 1, 1, 1)
        self.outfileButton = QtGui.QPushButton(self.audiobookPropertiesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outfileButton.sizePolicy().hasHeightForWidth())
        self.outfileButton.setSizePolicy(sizePolicy)
        self.outfileButton.setText("")
        self.outfileButton.setObjectName("outfileButton")
        self.gridLayout.addWidget(self.outfileButton, 15, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.audiobookPropertiesPage)
        self.chapterPropertiesPage = QtGui.QWidget()
        self.chapterPropertiesPage.setObjectName("chapterPropertiesPage")
        self.gridLayout_4 = QtGui.QGridLayout(self.chapterPropertiesPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtGui.QLabel(self.chapterPropertiesPage)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 2)
        self.label_9 = QtGui.QLabel(self.chapterPropertiesPage)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 2)
        self.chapterTitleEdit = QtGui.QLineEdit(self.chapterPropertiesPage)
        self.chapterTitleEdit.setObjectName("chapterTitleEdit")
        self.gridLayout_2.addWidget(self.chapterTitleEdit, 3, 0, 1, 2)
        spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem5, 4, 0, 1, 2)
        self.label_12 = QtGui.QLabel(self.chapterPropertiesPage)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 5, 0, 1, 2)
        self.startTimeEdit = QtGui.QLineEdit(self.chapterPropertiesPage)
        self.startTimeEdit.setEnabled(True)
        self.startTimeEdit.setReadOnly(True)
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.gridLayout_2.addWidget(self.startTimeEdit, 6, 0, 1, 2)
        self.label_10 = QtGui.QLabel(self.chapterPropertiesPage)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 2)
        self.durationEdit = QtGui.QLineEdit(self.chapterPropertiesPage)
        self.durationEdit.setReadOnly(True)
        self.durationEdit.setObjectName("durationEdit")
        self.gridLayout_2.addWidget(self.durationEdit, 8, 0, 1, 2)
        self.label_14 = QtGui.QLabel(self.chapterPropertiesPage)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 9, 0, 1, 2)
        self.endTimeEdit = QtGui.QLineEdit(self.chapterPropertiesPage)
        self.endTimeEdit.setReadOnly(True)
        self.endTimeEdit.setObjectName("endTimeEdit")
        self.gridLayout_2.addWidget(self.endTimeEdit, 10, 0, 1, 2)
        spacerItem6 = QtGui.QSpacerItem(45, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 11, 0, 1, 2)
        self.label_11 = QtGui.QLabel(self.chapterPropertiesPage)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 12, 0, 1, 2)
        self.chapterFileButton = QtGui.QPushButton(self.chapterPropertiesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chapterFileButton.sizePolicy().hasHeightForWidth())
        self.chapterFileButton.setSizePolicy(sizePolicy)
        self.chapterFileButton.setText("")
        self.chapterFileButton.setObjectName("chapterFileButton")
        self.gridLayout_2.addWidget(self.chapterFileButton, 13, 0, 1, 1)
        self.chapterFileEdit = QtGui.QLineEdit(self.chapterPropertiesPage)
        self.chapterFileEdit.setReadOnly(True)
        self.chapterFileEdit.setObjectName("chapterFileEdit")
        self.gridLayout_2.addWidget(self.chapterFileEdit, 13, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.chapterPropertiesPage)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.Toolbar = QtGui.QToolBar(MainWindow)
        self.Toolbar.setEnabled(True)
        self.Toolbar.setObjectName("Toolbar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.Toolbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionMoveDown = QtGui.QAction(MainWindow)
        self.actionMoveDown.setEnabled(False)
        self.actionMoveDown.setObjectName("actionMoveDown")
        self.actionRemove = QtGui.QAction(MainWindow)
        self.actionRemove.setEnabled(False)
        self.actionRemove.setObjectName("actionRemove")
        self.actionAddAudiobook = QtGui.QAction(MainWindow)
        self.actionAddAudiobook.setObjectName("actionAddAudiobook")
        self.actionAddChapter = QtGui.QAction(MainWindow)
        self.actionAddChapter.setEnabled(False)
        self.actionAddChapter.setObjectName("actionAddChapter")
        self.actionSortByFilename = QtGui.QAction(MainWindow)
        self.actionSortByFilename.setEnabled(False)
        self.actionSortByFilename.setObjectName("actionSortByFilename")
        self.actionSortByTracknumber = QtGui.QAction(MainWindow)
        self.actionSortByTracknumber.setEnabled(False)
        self.actionSortByTracknumber.setObjectName("actionSortByTracknumber")
        self.actionSplit = QtGui.QAction(MainWindow)
        self.actionSplit.setEnabled(False)
        self.actionSplit.setObjectName("actionSplit")
        self.actionProcess = QtGui.QAction(MainWindow)
        self.actionProcess.setEnabled(False)
        self.actionProcess.setObjectName("actionProcess")
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.actionMoveUp_2 = QtGui.QAction(MainWindow)
        self.actionMoveUp_2.setEnabled(False)
        self.actionMoveUp_2.setObjectName("actionMoveUp_2")
        self.action_help = QtGui.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.menu_Sort.addAction(self.actionSortByFilename)
        self.menu_Sort.addAction(self.actionSortByTracknumber)
        self.menu_Edit.addAction(self.actionMoveUp_2)
        self.menu_Edit.addAction(self.actionMoveDown)
        self.menu_Edit.addAction(self.actionRemove)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionAddAudiobook)
        self.menu_Edit.addAction(self.actionSplit)
        self.menu_Edit.addAction(self.menu_Sort.menuAction())
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionAddChapter)
        self.menu_Help.addAction(self.action_help)
        self.menu_Help.addAction(self.action_About)
        self.menu_File.addAction(self.actionProcess)
        self.menu_File.addAction(self.actionExit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.Toolbar.addAction(self.actionProcess)
        self.Toolbar.addSeparator()
        self.Toolbar.addAction(self.actionMoveDown)
        self.Toolbar.addAction(self.actionMoveUp_2)
        self.Toolbar.addAction(self.actionRemove)
        self.Toolbar.addSeparator()
        self.Toolbar.addAction(self.actionAddAudiobook)
        self.Toolbar.addAction(self.actionAddChapter)
        self.label.setBuddy(self.authorEdit)
        self.label_2.setBuddy(self.titleEdit)
        self.label_3.setBuddy(self.yearEdit)
        self.label_5.setBuddy(self.faacEdit)
        self.label_4.setBuddy(self.outfileEdit)
        self.label_9.setBuddy(self.chapterTitleEdit)
        self.label_12.setBuddy(self.startTimeEdit)
        self.label_10.setBuddy(self.durationEdit)
        self.label_14.setBuddy(self.endTimeEdit)
        self.label_11.setBuddy(self.chapterFileEdit)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "m4baker", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Sort.setTitle(QtGui.QApplication.translate("MainWindow", "&Sort", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Bitstream Vera Sans\'; font-size:10pt; font-weight:600;\">Welcome to m4baker!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Bitstream Vera Sans\';\">To start, create a new audiobook by clicking &quot;add Audiobook&quot;. Every selected file will be a single chapter. T</span>he files id3tags are read automatically. If no tags are found, file information is guessed from the filename. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A<span style=\" font-family:\'Bitstream Vera Sans\';\">dd, remove, rearrange or sort chapters using the menu. Chapter and audiobook metadata and coverfiles can be adjusted using this sidebar. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Bitstream Vera Sans\';\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the ouput filename if the automatically generated one does not please you. Experienced users can adjust faacs quality settings in the faac command line. If no changes are made here faacs standard settings are used. These should be fine for most purposes. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If needed, the book can be automatically split into parts. The upper limit is 10 hours which should work with all iPod models.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Bitstream Vera Sans\';\">When done, hit &quot;Process!&quot; and all audiobooks you created will be encoded and tagged. </span>Depending on the number of files and audiobooks to process this might take a long time, so one coffee might not be enough. In this case, get a sixpack beer instead. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Bitstream Vera Sans\';\">For transferring the audiobooks to you ipod, gtkpod is recommended.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Edit audiobook properties</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Year", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Cover (click to change)", None, QtGui.QApplication.UnicodeUTF8))
        self.coverLabel.setText(QtGui.QApplication.translate("MainWindow", "(click to change)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "faac command line", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Output file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Edit chapter properties</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Start time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "End time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.Toolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMoveDown.setText(QtGui.QApplication.translate("MainWindow", "Move &down", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setText(QtGui.QApplication.translate("MainWindow", "&Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddAudiobook.setText(QtGui.QApplication.translate("MainWindow", "Add &Audiobook", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddChapter.setText(QtGui.QApplication.translate("MainWindow", "Add &Chapter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSortByFilename.setText(QtGui.QApplication.translate("MainWindow", "Chapters by file&name", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSortByTracknumber.setText(QtGui.QApplication.translate("MainWindow", "Chapters by track&number", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSplit.setText(QtGui.QApplication.translate("MainWindow", "S&plit Audiobook", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProcess.setText(QtGui.QApplication.translate("MainWindow", "&Process all!", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMoveUp_2.setText(QtGui.QApplication.translate("MainWindow", "Move &up", None, QtGui.QApplication.UnicodeUTF8))
        self.action_help.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_help.setToolTip(QtGui.QApplication.translate("MainWindow", "get help", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

