from configuracion.listas import porcentajes
import numpy as np


def validar_requisito_4(obj, ):
    """Procedimiento de clase para verificar cumplimiento de requisito 4 (% invertido en capacitacion)
    recibe self desde la clase
    validar_requisito_4(self, )"""
    try:
        dividir = (float(obj.lineEdit.text()) / float(obj.input_facturacion.text())) * 100
        dividir = np.round(dividir, 3)
        if not obj.checkBox.isChecked():
            dividir = dividir
        else:
            dividir = dividir * 2
        if obj.combo_tipo_empresa.currentText() == porcentajes[0][0]:
            if dividir >= porcentajes[0][1]:
                obj.verificacion['requisito_4'] = 'Cumple'
            else:
                obj.verificacion['requisito_4'] = 'No Cumple'
        elif obj.combo_tipo_empresa.currentText() == porcentajes[1][0]:
            if dividir >= porcentajes[1][1]:
                obj.verificacion['requisito_4'] = 'Cumple'
            else:
                obj.verificacion['requisito_4'] = 'No Cumple'
        elif obj.combo_tipo_empresa.currentText() == porcentajes[2][0]:
            if dividir >= porcentajes[2][1]:
                obj.verificacion['requisito_4'] = 'Cumple'
            else:
                obj.verificacion['requisito_4'] = 'No Cumple'
        else:
            obj.verificacion['requisito_4'] = 'No se identifico el tipo de empresa'
    except Exception as e:
        print(e)
