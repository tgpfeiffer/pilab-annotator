# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'annotator.ui'
#
# Created: Tue Jul 20 16:13:28 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(921, 599)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        mainWindow.setFont(font)
        mainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 591, 511))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMouseTracking(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.image = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.image.setCursor(QtCore.Qt.CrossCursor)
        self.image.setMouseTracking(True)
        self.image.setText("")
        self.image.setObjectName("image")
        self.horizontalLayout_4.addWidget(self.image)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 921, 22))
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(10)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.fileMenu = QtGui.QMenu(self.menuBar)
        self.fileMenu.setObjectName("fileMenu")
        self.viewMenu = QtGui.QMenu(self.menuBar)
        self.viewMenu.setObjectName("viewMenu")
        self.windowsMenu = QtGui.QMenu(self.viewMenu)
        self.windowsMenu.setObjectName("windowsMenu")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menuBar)
        self.toolBox = QtGui.QDockWidget(mainWindow)
        self.toolBox.setEnabled(True)
        self.toolBox.setMinimumSize(QtCore.QSize(0, 100))
        self.toolBox.setMaximumSize(QtCore.QSize(524287, 100))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName("toolBox")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayoutWidget = QtGui.QWidget(self.dockWidgetContents_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 101, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dotButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.dotButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dotButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/ps_icons/AddAnchorPoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dotButton.setIcon(icon)
        self.dotButton.setIconSize(QtCore.QSize(30, 23))
        self.dotButton.setCheckable(True)
        self.dotButton.setObjectName("dotButton")
        self.horizontalLayout.addWidget(self.dotButton)
        self.rectangleButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.rectangleButton.setEnabled(True)
        self.rectangleButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rectangleButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("graphics/ps_icons/Rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rectangleButton.setIcon(icon1)
        self.rectangleButton.setIconSize(QtCore.QSize(30, 23))
        self.rectangleButton.setCheckable(True)
        self.rectangleButton.setObjectName("rectangleButton")
        self.horizontalLayout.addWidget(self.rectangleButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolBox.setWidget(self.dockWidgetContents_2)
        mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.toolBox)
        self.optionBox = QtGui.QDockWidget(mainWindow)
        self.optionBox.setMinimumSize(QtCore.QSize(0, 200))
        self.optionBox.setMaximumSize(QtCore.QSize(524287, 200))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.optionBox.setFont(font)
        self.optionBox.setObjectName("optionBox")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.dockWidgetContents_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 51, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rectClickButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.rectClickButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rectClickButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("graphics/ps_icons/RectangularMarquee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rectClickButton.setIcon(icon2)
        self.rectClickButton.setIconSize(QtCore.QSize(30, 23))
        self.rectClickButton.setCheckable(True)
        self.rectClickButton.setChecked(True)
        self.rectClickButton.setObjectName("rectClickButton")
        self.verticalLayout_2.addWidget(self.rectClickButton)
        self.rectDragButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.rectDragButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rectDragButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("graphics/ps_icons/Move.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rectDragButton.setIcon(icon3)
        self.rectDragButton.setIconSize(QtCore.QSize(30, 23))
        self.rectDragButton.setCheckable(True)
        self.rectDragButton.setObjectName("rectDragButton")
        self.verticalLayout_2.addWidget(self.rectDragButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.dockWidgetContents_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 51, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dotClickButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.dotClickButton.setEnabled(False)
        self.dotClickButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dotClickButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("graphics/ps_icons/Pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dotClickButton.setIcon(icon4)
        self.dotClickButton.setIconSize(QtCore.QSize(30, 23))
        self.dotClickButton.setCheckable(True)
        self.dotClickButton.setChecked(True)
        self.dotClickButton.setObjectName("dotClickButton")
        self.verticalLayout_3.addWidget(self.dotClickButton)
        self.dotDragButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.dotDragButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dotDragButton.setText("")
        self.dotDragButton.setIcon(icon3)
        self.dotDragButton.setIconSize(QtCore.QSize(30, 23))
        self.dotDragButton.setCheckable(True)
        self.dotDragButton.setObjectName("dotDragButton")
        self.verticalLayout_3.addWidget(self.dotDragButton)
        self.dotUndoButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.dotUndoButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dotUndoButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("graphics/ps_icons/Eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dotUndoButton.setIcon(icon5)
        self.dotUndoButton.setIconSize(QtCore.QSize(30, 23))
        self.dotUndoButton.setCheckable(False)
        self.dotUndoButton.setObjectName("dotUndoButton")
        self.verticalLayout_3.addWidget(self.dotUndoButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.optionBox.setWidget(self.dockWidgetContents_3)
        mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.optionBox)
        self.zoomBox = QtGui.QDockWidget(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.zoomBox.setFont(font)
        self.zoomBox.setObjectName("zoomBox")
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.zoomImage = QtGui.QLabel(self.dockWidgetContents_4)
        self.zoomImage.setMinimumSize(QtCore.QSize(200, 200))
        self.zoomImage.setMaximumSize(QtCore.QSize(200, 200))
        self.zoomImage.setText("")
        self.zoomImage.setObjectName("zoomImage")
        self.verticalLayout_4.addWidget(self.zoomImage)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.zoomBox.setWidget(self.dockWidgetContents_4)
        mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.zoomBox)
        self.statusBar = QtGui.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.navigationBox = QtGui.QDockWidget(mainWindow)
        self.navigationBox.setMinimumSize(QtCore.QSize(150, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.navigationBox.setFont(font)
        self.navigationBox.setObjectName("navigationBox")
        self.dockWidgetContents_6 = QtGui.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.verticalLayoutWidget = QtGui.QWidget(self.dockWidgetContents_6)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 151, 122))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prevButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.prevButton.setObjectName("prevButton")
        self.horizontalLayout_2.addWidget(self.prevButton)
        self.nextButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.firstButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.firstButton.setObjectName("firstButton")
        self.horizontalLayout_3.addWidget(self.firstButton)
        self.minusTenButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.minusTenButton.setObjectName("minusTenButton")
        self.horizontalLayout_3.addWidget(self.minusTenButton)
        self.plusTenButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.plusTenButton.setObjectName("plusTenButton")
        self.horizontalLayout_3.addWidget(self.plusTenButton)
        self.lastButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.lastButton.setObjectName("lastButton")
        self.horizontalLayout_3.addWidget(self.lastButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.imageComboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.imageComboBox.setObjectName("imageComboBox")
        self.verticalLayout.addWidget(self.imageComboBox)
        self.indexLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.indexLabel.setObjectName("indexLabel")
        self.verticalLayout.addWidget(self.indexLabel)
        self.navigationBox.setWidget(self.dockWidgetContents_6)
        mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.navigationBox)
        self.openAction = QtGui.QAction(mainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openAction.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.openAction.setFont(font)
        self.openAction.setObjectName("openAction")
        self.exitAction = QtGui.QAction(mainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitAction.setIcon(icon7)
        self.exitAction.setObjectName("exitAction")
        self.toolboxAction = QtGui.QAction(mainWindow)
        self.toolboxAction.setCheckable(True)
        self.toolboxAction.setChecked(True)
        self.toolboxAction.setObjectName("toolboxAction")
        self.optionsAction = QtGui.QAction(mainWindow)
        self.optionsAction.setCheckable(True)
        self.optionsAction.setChecked(True)
        self.optionsAction.setObjectName("optionsAction")
        self.zoomAction = QtGui.QAction(mainWindow)
        self.zoomAction.setCheckable(True)
        self.zoomAction.setChecked(True)
        self.zoomAction.setObjectName("zoomAction")
        self.navigationAction = QtGui.QAction(mainWindow)
        self.navigationAction.setCheckable(True)
        self.navigationAction.setChecked(True)
        self.navigationAction.setObjectName("navigationAction")
        self.indicesAction = QtGui.QAction(mainWindow)
        self.indicesAction.setCheckable(True)
        self.indicesAction.setObjectName("indicesAction")
        self.actionAbout = QtGui.QAction(mainWindow)
        self.actionAbout.setEnabled(False)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(mainWindow)
        self.actionHelp.setEnabled(False)
        self.actionHelp.setObjectName("actionHelp")
        self.saveAction = QtGui.QAction(mainWindow)
        self.saveAction.setCheckable(False)
        self.saveAction.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.saveAction.setObjectName("saveAction")
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.windowsMenu.addAction(self.toolboxAction)
        self.windowsMenu.addAction(self.optionsAction)
        self.windowsMenu.addAction(self.zoomAction)
        self.windowsMenu.addAction(self.navigationAction)
        self.viewMenu.addAction(self.windowsMenu.menuAction())
        self.viewMenu.addAction(self.indicesAction)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuBar.addAction(self.fileMenu.menuAction())
        self.menuBar.addAction(self.viewMenu.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QObject.connect(self.exitAction, QtCore.SIGNAL("triggered()"), mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Annotator", None, QtGui.QApplication.UnicodeUTF8))
        self.fileMenu.setTitle(QtGui.QApplication.translate("mainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.viewMenu.setTitle(QtGui.QApplication.translate("mainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.windowsMenu.setTitle(QtGui.QApplication.translate("mainWindow", "Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("mainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Toolbox", None, QtGui.QApplication.UnicodeUTF8))
        self.dotButton.setToolTip(QtGui.QApplication.translate("mainWindow", "Point tool", None, QtGui.QApplication.UnicodeUTF8))
        self.rectangleButton.setToolTip(QtGui.QApplication.translate("mainWindow", "Rectangle tool", None, QtGui.QApplication.UnicodeUTF8))
        self.optionBox.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.rectClickButton.setToolTip(QtGui.QApplication.translate("mainWindow", "Draw", None, QtGui.QApplication.UnicodeUTF8))
        self.rectDragButton.setToolTip(QtGui.QApplication.translate("mainWindow", "Drag", None, QtGui.QApplication.UnicodeUTF8))
        self.dotClickButton.setToolTip(QtGui.QApplication.translate("mainWindow", "Draw", None, QtGui.QApplication.UnicodeUTF8))
        self.dotDragButton.setToolTip(QtGui.QApplication.translate("mainWindow", "Drag", None, QtGui.QApplication.UnicodeUTF8))
        self.dotUndoButton.setToolTip(QtGui.QApplication.translate("mainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.dotUndoButton.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomBox.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.navigationBox.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.prevButton.setToolTip(QtGui.QApplication.translate("mainWindow", "Previous image", None, QtGui.QApplication.UnicodeUTF8))
        self.prevButton.setText(QtGui.QApplication.translate("mainWindow", "-1", None, QtGui.QApplication.UnicodeUTF8))
        self.prevButton.setShortcut(QtGui.QApplication.translate("mainWindow", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setToolTip(QtGui.QApplication.translate("mainWindow", "Next image", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("mainWindow", "+1", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setShortcut(QtGui.QApplication.translate("mainWindow", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.firstButton.setToolTip(QtGui.QApplication.translate("mainWindow", "First image", None, QtGui.QApplication.UnicodeUTF8))
        self.firstButton.setText(QtGui.QApplication.translate("mainWindow", "|<", None, QtGui.QApplication.UnicodeUTF8))
        self.firstButton.setShortcut(QtGui.QApplication.translate("mainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.minusTenButton.setToolTip(QtGui.QApplication.translate("mainWindow", "10 images back", None, QtGui.QApplication.UnicodeUTF8))
        self.minusTenButton.setText(QtGui.QApplication.translate("mainWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.minusTenButton.setShortcut(QtGui.QApplication.translate("mainWindow", "PgUp", None, QtGui.QApplication.UnicodeUTF8))
        self.plusTenButton.setToolTip(QtGui.QApplication.translate("mainWindow", "10 images forward", None, QtGui.QApplication.UnicodeUTF8))
        self.plusTenButton.setText(QtGui.QApplication.translate("mainWindow", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.plusTenButton.setShortcut(QtGui.QApplication.translate("mainWindow", "PgDown", None, QtGui.QApplication.UnicodeUTF8))
        self.lastButton.setToolTip(QtGui.QApplication.translate("mainWindow", "Last image", None, QtGui.QApplication.UnicodeUTF8))
        self.lastButton.setText(QtGui.QApplication.translate("mainWindow", ">|", None, QtGui.QApplication.UnicodeUTF8))
        self.lastButton.setShortcut(QtGui.QApplication.translate("mainWindow", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.indexLabel.setText(QtGui.QApplication.translate("mainWindow", "(0 / 0)", None, QtGui.QApplication.UnicodeUTF8))
        self.openAction.setText(QtGui.QApplication.translate("mainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.openAction.setStatusTip(QtGui.QApplication.translate("mainWindow", "Open a directory containing images", None, QtGui.QApplication.UnicodeUTF8))
        self.openAction.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAction.setText(QtGui.QApplication.translate("mainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAction.setStatusTip(QtGui.QApplication.translate("mainWindow", "Exit application", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAction.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.toolboxAction.setText(QtGui.QApplication.translate("mainWindow", "Toolbox", None, QtGui.QApplication.UnicodeUTF8))
        self.optionsAction.setText(QtGui.QApplication.translate("mainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomAction.setText(QtGui.QApplication.translate("mainWindow", "Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.navigationAction.setText(QtGui.QApplication.translate("mainWindow", "Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.indicesAction.setText(QtGui.QApplication.translate("mainWindow", "Indices", None, QtGui.QApplication.UnicodeUTF8))
        self.indicesAction.setShortcut(QtGui.QApplication.translate("mainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("mainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("mainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setShortcut(QtGui.QApplication.translate("mainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAction.setText(QtGui.QApplication.translate("mainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAction.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))

