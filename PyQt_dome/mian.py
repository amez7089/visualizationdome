# -*- coding=utf-8 -*-
# @Time     :2018/12/21 16:44
# @Author   :ZhouChuqi
# !/usr/bin/env python3

import sys
import hello

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = hello.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
