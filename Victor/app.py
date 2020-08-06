from check_list_ui import *
from configuracion.listas import actividades, tipos_de_empresas, combo_si_no
from requisitos import validar_formulario
import numpy as np
from PyQt5.QtWidgets import QDialog, QMessageBox
import os


class CheckList(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, ):
        super(CheckList, self).__init__()
        self.setupUi(self)
        self.combo_tipo_empresa.addItems(tipos_de_empresas)
        self.combo_actividades.addItems(actividades)
        self.comboBox.addItems(combo_si_no)
        self.pushButton_2.clicked.connect(self.ver_porcentaje)
        self.verificacion = {}
        self.pushButton.clicked.connect(self.validacion)

    def ver_porcentaje(self, ):
        try:
            division = (float(self.lineEdit_2.text())/float(self.input_facturacion.text()))*100
            division = np.round(division, 2)
            string = str(division) + ' %'
            self.porcentaje_asignado.setText(string)
        except Exception as e:
            print(e)

    def validacion(self,):
        texto, cuit = validar_formulario.validar_formulario(self, )
        directorio = './resultados/'
        if not os.path.exists(directorio):
            os.mkdir(directorio)
        file = open(f"{directorio}resultado {cuit}.docx", "w")
        file.write(texto)
        file.close()
        QMessageBox.about(self, 'Resultado', texto)


class Popup(QDialog):

    def __init__(self, *args, **kwargs):
        super(Popup, self).__init__(*args, **kwargs)
        self.setWindowTitle('Resultado')
        self.setFixedSize(300, 600)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = CheckList()
    window.show()
    app.exec_()
