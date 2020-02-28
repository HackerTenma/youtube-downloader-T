import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from gui.main import Ui_MainWindow

from paquete.descargar import *
import pyperclip

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)


def my_hook(d):
    if d['status'] == 'downloading':
        p = d['_percent_str']
        p = p.replace('%', '')
        ui.progressBar.setValue(float(p))
    elif d['status'] == 'finished':
        ui.lineEdit_directorio.setText("")
        ui.lineEdit_link.setText("")


def on_click1():
    ui.lineEdit_link.setText(pyperclip.paste())


def on_click2():
    filename = QFileDialog.getSaveFileName()
    if filename:
        ui.lineEdit_directorio.setText(filename[0])


def on_click3():
    download(ui.lineEdit_directorio.text(), ui.lineEdit_link.text(), my_hook)


def check_text():
    if ui.lineEdit_link.text() != "" and ui.lineEdit_directorio.text() != "":
        ui.pushButton_descargar.setEnabled(True)
    else:
        ui.pushButton_descargar.setEnabled(False)


ui.pushButton_pegar.clicked.connect(on_click1)
ui.pushButton_guardar.clicked.connect(on_click2)
ui.pushButton_descargar.clicked.connect(on_click3)

ui.lineEdit_link.textChanged.connect(check_text)
ui.lineEdit_directorio.textChanged.connect(check_text)

window.show()
sys.exit(app.exec_())
