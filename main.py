#
# Created by JLT on 29/09/2017.
#
import sys

from PyQt5 import QtWidgets

from timerui_leet import Ui_PCRtimer


# starts the GUI and has it running until the window is closed
def main():

    app = QtWidgets.QApplication(sys.argv)
    PCRtimer = QtWidgets.QDialog()
    ui = Ui_PCRtimer()
    ui.setupUi(PCRtimer)
    PCRtimer.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
