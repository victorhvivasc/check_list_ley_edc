from check_list_ui import *
from listas import actividades, tipos_de_empresas, combo_si_no, porcentajes
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
        self.pushButton.clicked.connect(self.validar_formulario)

    def ver_porcentaje(self, ):
        try:
            division = (float(self.lineEdit_2.text())/float(self.input_facturacion.text()))*100
            division = np.round(division, 2)
            string = str(division) + ' %'
            self.porcentaje_asignado.setText(string)
        except Exception as e:
            print(e)

    def validar_requisito_1(self,):
        try:
            division = (float(self.lineEdit_2.text())/float(self.input_facturacion.text()))*100
            self.porcentaje_asignado.setText(str(division))
            if division >= 70:
                self.verificacion['requisito_1'] = 'Cumple'
            else:
                self.verificacion['requisito_1'] = 'No Cumple'
        except Exception as e:
            self.verificacion['requisito_1'] = 'No indicado'
            print(e)

    def validar_requisito_2(self,):
        try:
            if self.radio_presenta.isChecked():
                self.verificacion['requisito_2'] = 'Cumple'
            else:
                self.verificacion['requisito_2'] = 'No Cumple'
        except Exception as e:
            print(e)

    def validar_requisito_3(self,):
        try:
            if self.comboBox.currentText() == 'SÍ':
                self.verificacion['requisito_3'] = 'Cumple'
            else:
                self.verificacion['requisito_3'] = 'No Cumple'
        except Exception as e:
            self.verificacion['requisito_3'] = 'No indicado'
            print(e)

    def validar_requisito_4(self,):
        try:
            dividir = (float(self.lineEdit.text()) / float(self.input_facturacion.text())) * 100
            dividir = np.round(dividir, 3)
            if not self.checkBox.isChecked():
                dividir = dividir
            else:
                dividir = dividir*2
            if self.combo_tipo_empresa.currentText() == porcentajes[0][0]:
                if dividir >= porcentajes[0][1]:
                    self.verificacion['requisito_4'] = 'Cumple'
                else:
                    self.verificacion['requisito_4'] = 'No Cumple'
            elif self.combo_tipo_empresa.currentText() == porcentajes[1][0]:
                if dividir >= porcentajes[1][1]:
                    self.verificacion['requisito_4'] = 'Cumple'
                else:
                    self.verificacion['requisito_4'] = 'No Cumple'
            elif self.combo_tipo_empresa.currentText() == porcentajes[2][0]:
                if dividir >= porcentajes[2][1]:
                    self.verificacion['requisito_4'] = 'Cumple'
                else:
                    self.verificacion['requisito_4'] = 'No Cumple'
            else:
                self.verificacion['requisito_4'] = 'No se identifico el tipo de empresa'
        except Exception as e:
            print(e)

    def validar_requisito_5(self,):
        try:
            dividir = (float(self.lineEdit_3.text()) / float(self.input_facturacion.text()))*100
            dividir = np.round(dividir, 3)
            if self.combo_tipo_empresa.currentText() == porcentajes[0][0]:
                if dividir >= porcentajes[0][2]:
                    self.verificacion['requisito_5'] = 'Cumple'
                else:
                    self.verificacion['requisito_5'] = 'No Cumple'
            elif self.combo_tipo_empresa.currentText() == porcentajes[1][0]:
                if dividir >= porcentajes[1][2]:
                    self.verificacion['requisito_5'] = 'Cumple'
                else:
                    self.verificacion['requisito_5'] = 'No Cumple'
            elif self.combo_tipo_empresa.currentText() == porcentajes[2][0]:
                if dividir >= porcentajes[2][2]:
                    self.verificacion['requisito_5'] = 'Cumple'
                else:
                    self.verificacion['requisito_5'] = 'No Cumple'
            else:
                self.verificacion['requisito_5'] = 'No se identifico el tipo de empresa'
        except Exception as e:
            print(e)

    def validar_requisito_6(self,):
        try:
            dividir = (float(self.lineEdit_4.text()) / float(self.input_facturacion.text()))*100
            dividir = np.round(dividir, 3)
            if self.combo_tipo_empresa.currentText() == porcentajes[0][0]:
                if dividir >= porcentajes[0][3]:
                    self.verificacion['requisito_6'] = 'Cumple'
                else:
                    self.verificacion['requisito_6'] = 'No Cumple'
            elif self.combo_tipo_empresa.currentText() == porcentajes[1][0]:
                if dividir >= porcentajes[1][3]:
                    self.verificacion['requisito_6'] = 'Cumple'
                else:
                    self.verificacion['requisito_6'] = 'No Cumple'
            elif self.combo_tipo_empresa.currentText() == porcentajes[2][0]:
                if dividir >= porcentajes[2][3]:
                    self.verificacion['requisito_6'] = 'Cumple'
                else:
                    self.verificacion['requisito_6'] = 'No Cumple'
            else:
                self.verificacion['requisito_6'] = 'No se identifico el tipo de empresa'
        except Exception as e:
            print(e)

    def validar_formulario(self,):
        self.validar_requisito_1()
        self.validar_requisito_2()
        self.validar_requisito_3()
        self.validar_requisito_4()
        self.validar_requisito_5()
        self.validar_requisito_6()
        cumple = ''
        no_cumple = ''
        for x in self.verificacion:
            if self.verificacion[x] == 'Cumple':
                cumple += ' ' + x
            else:
                no_cumple += ' ' + x
        nombre, cuit = self.input_nombre_empresa.text(), self.input_cuit.text()
        tipo, activ = self.combo_tipo_empresa.currentText(), self.combo_actividades.currentText()
        r1, r2 = self.porcentaje_asignado.text(), self.verificacion['requisito_2']
        r3, r4 = self.comboBox.currentText(), self.lineEdit.text()
        r5, r6 = self.lineEdit_3.text(), self.lineEdit_4.text()
        texto = f"""Para la empresa: {nombre} 
    poseedora del CUIT número: {cuit} 
    declarada: {tipo} 
    que desarrolla las actividades: {activ}.

    se identifico el siguiente cumplimiento de requisitos:

    1.- % de facturación declarado: {r1} %.
    2.- Acreditación del desarrollo de actividades promovidas de manera intensiva para incorporar conocimiento: 
    {r2}.
    3.- Acredita la realización de mejoras continuas en la calidad de sus servicios, productos y/o procesos, 
    o mediante una norma de calidad reconocida aplicable a sus servicios, productos y/o procesos: 
    {r3}.
    4.- Acreditar capacitación de sus empleados y/o destinatarios en general en temáticas relacionadas con 
    la economía del  conocimiento en un porcentaje respecto de su masa salarial del último año: 
    {r4} AR$.
    5.- Investigación y desarrollo (que incluya novedad, originalidad y/o creatividad) en un porcentaje 
    respecto de su facturación total del último año: 
    {r5} AR$.
    6.- Acreditar la realización de exportaciones de bienes y/o servicios que surjan del desarrollo de alguna 
    de las actividades promovidas y/o del desarrollo y aplicación intensiva de las mismas en un porcentaje
    respecto de su facturación total del último año: 
    {r6} AR$.
    """
        texto1 = texto + '\n\n' + "Cumple los requisitos: " + str(cumple) + '\n' + "No Cumple los requisitos: " \
                                                                                   + str(no_cumple) + '\n'
        directorio = './resultados/'
        if not os.path.exists(directorio):
            os.mkdir(directorio)
        file = open(f"{directorio}resultado {cuit}.docx", "w")
        file.write(texto1)
        file.close()
        QMessageBox.about(self, 'Resultado', texto1)


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
