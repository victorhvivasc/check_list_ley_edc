from configuracion.listas import porcentajes
import numpy as np


def validar_requisito_6(self, ):
    """Procedimiento de clase para verificar cumplimiento de requisito 6 (% de exportacion)
    recibe self desde la clase
    validar_requisito_6(self, )"""
    try:
        dividir = (float(self.lineEdit_4.text()) / float(self.input_facturacion.text())) * 100
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
