#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the main module."""

import logging
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from {{ package }}.main import Ui_MainWindow

logger = logging.getLogger(__name__)


class Example(object):
    """This is an example class."""
    PI = 3.14

    x = 0

    def __init__(self):
        self.x = 0

    def add(self, y):
        self.x += y

    @classmethod
    def sub(cls, y):
        cls.x -= y

    @staticmethod
    def mul(y):
        Example.x *= y

    # `xx` Public; `_xx` Protected;
    # `__xx` Private; `__xx__` Built-in
    def _div(self, y=1):
        self.x /= y


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator()
    translator.load(':/static/i18n/qt_zh_CN.qm')
    app.installTranslator(translator)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
