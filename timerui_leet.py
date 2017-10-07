# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.6
#
# This file contains the PyQt UI and functions which call the actual calculator functions

from random import randint

from PyQt5 import QtCore, QtGui, QtWidgets

from presets import presets, enzymelist
from calculator import *

# automatically generated object with encapsulates the GUI parameters and methods
class Ui_PCRtimer(object):

    # sets up the GUI
    def setupUi(self, PCRtimer):
        PCRtimer.setObjectName("PCRtimer")
        PCRtimer.resize(540, 404)
        PCRtimer.setMinimumSize(QtCore.QSize(540, 404))
        PCRtimer.setMaximumSize(QtCore.QSize(540, 404))
        self.presetbox = QtWidgets.QComboBox(PCRtimer)
        self.presetbox.setGeometry(QtCore.QRect(290, 270, 201, 61))
        largefont = QtGui.QFont()
        largefont.setPointSize(10)
        smallfont = QtGui.QFont()
        smallfont.setPointSize(7)
        self.presetbox.setFont(largefont)
        self.presetbox.setObjectName("presetbox")
        self.presetbox.addItems(enzymelist)

        self.label = QtWidgets.QLabel(PCRtimer)
        self.label.setGeometry(QtCore.QRect(410, 20, 51, 19))
        self.label.setObjectName("label")
        self.label.setFont(smallfont)

        self.melt_2 = QtWidgets.QSpinBox(PCRtimer)
        self.melt_2.setGeometry(QtCore.QRect(30, 130, 81, 31))
        self.melt_2.setObjectName("melt_2")

        self.label_2 = QtWidgets.QLabel(PCRtimer)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 71, 19))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(smallfont)


        self.label_5 = QtWidgets.QLabel(PCRtimer)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 101, 20))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(smallfont)

        self.initmelt = QtWidgets.QSpinBox(PCRtimer)
        self.initmelt.setGeometry(QtCore.QRect(30, 50, 81, 31))
        self.initmelt.setObjectName("initmelt")

        self.cycles = QtWidgets.QSpinBox(PCRtimer)
        self.cycles.setGeometry(QtCore.QRect(410, 50, 81, 31))
        self.cycles.setObjectName("cycles")

        self.finalext = QtWidgets.QSpinBox(PCRtimer)
        self.finalext.setGeometry(QtCore.QRect(220, 50, 81, 31))
        self.finalext.setObjectName("finalext")

        self.label_6 = QtWidgets.QLabel(PCRtimer)
        self.label_6.setGeometry(QtCore.QRect(220, 20, 111, 20))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(smallfont)

        self.label_7 = QtWidgets.QLabel(PCRtimer)
        self.label_7.setGeometry(QtCore.QRect(290, 240, 68, 19))
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(smallfont)

        self.label_4 = QtWidgets.QLabel(PCRtimer)
        self.label_4.setGeometry(QtCore.QRect(120, 50, 16, 31))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(smallfont)


        self.label_8 = QtWidgets.QLabel(PCRtimer)
        self.label_8.setGeometry(QtCore.QRect(310, 50, 16, 31))
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(smallfont)

        self.label_10 = QtWidgets.QLabel(PCRtimer)
        self.label_10.setGeometry(QtCore.QRect(120, 130, 16, 31))
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(smallfont)

        self.label_9 = QtWidgets.QLabel(PCRtimer)
        self.label_9.setGeometry(QtCore.QRect(220, 100, 111, 19))
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(smallfont)

        self.label_12 = QtWidgets.QLabel(PCRtimer)
        self.label_12.setGeometry(QtCore.QRect(310, 130, 16, 31))
        self.label_12.setObjectName("label_12")
        self.label_12.setFont(smallfont)

        self.anneal = QtWidgets.QSpinBox(PCRtimer)
        self.anneal.setGeometry(QtCore.QRect(220, 130, 81, 31))
        self.anneal.setObjectName("anneal")

        self.extend = QtWidgets.QSpinBox(PCRtimer)
        self.extend.setGeometry(QtCore.QRect(410, 130, 81, 31))
        self.extend.setObjectName("extend")

        self.label_13 = QtWidgets.QLabel(PCRtimer)
        self.label_13.setGeometry(QtCore.QRect(500, 130, 20, 31))
        self.label_13.setObjectName("label_13")
        self.label_13.setFont(smallfont)

        self.label_3 = QtWidgets.QLabel(PCRtimer)
        self.label_3.setGeometry(QtCore.QRect(410, 100, 101, 19))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(smallfont)

        self.fidelity = QtWidgets.QDial(PCRtimer)
        self.fidelity.setGeometry(QtCore.QRect(70, 200, 151, 151))
        self.fidelity.setSliderPosition(75)
        self.fidelity.setOrientation(QtCore.Qt.Horizontal)
        self.fidelity.setNotchesVisible(True)
        self.fidelity.setObjectName("fidelity")

        self.label_11 = QtWidgets.QLabel(PCRtimer)
        self.label_11.setGeometry(QtCore.QRect(50, 330, 55, 45))
        self.label_11.setObjectName("label_11")
        self.label_11.setFont(smallfont)

        self.label_14 = QtWidgets.QLabel(PCRtimer)
        self.label_14.setGeometry(QtCore.QRect(190, 350, 35, 123))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_14.setFont(smallfont)

        self.label_15 = QtWidgets.QLabel(PCRtimer)
        self.label_15.setGeometry(QtCore.QRect(190, 330, 55, 45))
        self.label_15.setObjectName("label_15")
        self.label_15.setFont(smallfont)

        self.lineEdit = QtWidgets.QLineEdit(PCRtimer)
        self.lineEdit.setGeometry(QtCore.QRect(290, 350, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(smallfont)


        self.label_16 = QtWidgets.QLabel(PCRtimer)
        self.label_16.setGeometry(QtCore.QRect(410, 180, 81, 30))
        self.label_16.setObjectName("label_16")
        self.label_16.setFont(smallfont)

        self.label_17 = QtWidgets.QLabel(PCRtimer)
        self.label_17.setGeometry(QtCore.QRect(499, 210, 21, 31))
        self.label_17.setObjectName("label_17")
        self.label_17.setFont(smallfont)

        self.kbp = QtWidgets.QDoubleSpinBox(PCRtimer)
        self.kbp.setGeometry(QtCore.QRect(410, 210, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.kbp.setFont(font)
        self.kbp.setObjectName("kbp")

        ## defined connections between GUI elements and functions to be executed
        self.presetbox.activated[str].connect(self.setpreset)
        self.anneal.valueChanged[int].connect(self.calc)
        self.melt_2.valueChanged[int].connect(self.calc)
        self.initmelt.valueChanged[int].connect(self.calc)
        self.extend.valueChanged[int].connect(self.calc)
        self.finalext.valueChanged[int].connect(self.calc)
        self.cycles.valueChanged[int].connect(self.calc)
        self.fidelity.valueChanged[int].connect(self.tune_fidelity)
        self.kbp.valueChanged[float].connect(self.calc)

        self.initialize_special_class_variables()
        self.retranslateUi(PCRtimer)
        QtCore.QMetaObject.connectSlotsByName(PCRtimer)

    def retranslateUi(self, PCRtimer):
        _translate = QtCore.QCoreApplication.translate
        PCRtimer.setWindowTitle(_translate("PCRtimer", "PCRtimer"))
        self.label.setText(_translate("PCRtimer", "Cycles"))
        self.label_2.setText(_translate("PCRtimer", "Melting time"))
        self.label_5.setText(_translate("PCRtimer", "Initial melting"))
        self.label_6.setText(_translate("PCRtimer", "Final extension"))
        self.label_7.setText(_translate("PCRtimer", "Presets"))
        self.label_4.setText(_translate("PCRtimer", "s"))
        self.label_8.setText(_translate("PCRtimer", "s"))
        self.label_10.setText(_translate("PCRtimer", "s"))
        self.label_9.setText(_translate("PCRtimer", "Annealing time"))
        self.label_12.setText(_translate("PCRtimer", "s"))
        self.label_13.setText(_translate("PCRtimer", "s"))
        self.label_3.setText(_translate("PCRtimer", "Extension/kb"))
        self.label_11.setText(_translate("PCRtimer", "go home\nearly"))
        self.label_15.setText(_translate("PCRtimer", "go home\nfor sure"))
        self.label_16.setText(_translate("PCRtimer", "Product size"))
        self.label_17.setText(_translate("PCRtimer", "kb"))

    # custom method which packages all number input boxes into a list
    def initialize_special_class_variables(self):
        self.boxes = [self.initmelt, self.finalext, self.melt_2,
                      self.anneal, self.extend, self.cycles]

    # custom method which sends the values from number input boxes to a function to calculate PCR time
    def calc(self):
        # TODO: check for validity of input before calculating, especially with respect to the picked enzyme
        currentvals = [x.value() for x in self.boxes]
        if 0 in currentvals or self.kbp.value() == 0:
            result = "Invalid: Params can't be 0"
        else:
            ## calculate end time from current settings
            #calcres = mcalc(currentvals, self.kbp.value())  # not yet implemented
            calcres = randint(1,4)
            result = "Expected duration: %s" % calcres
            #result = "Expected Duration: %s h" % str(sum(currentvals) // 6)

        self.lineEdit.setText(result)

    # custom method which sends values from number input boxes and the dial setting to a function to calculate new values
    def tune_fidelity(self):
        currentvals = [x.value() for x in self.boxes]
        dialsetting = self.fidelity.value()

        ## calculate the new setting from current values and dial setting
        #result = kfidelity(currentvals, dialsetting)  # not yet implemented
        result = [randint(10,100) for x in range(6)]

        [x.setValue(result[i]) for i, x in enumerate(self.boxes)]
        self.calc()

    # updates number input box values depending on the selected preset
    def setpreset(self, s):
        picked = presets[s]
        [x.setValue(picked[i]) for i, x in enumerate(self.boxes)]
        self.calc()
