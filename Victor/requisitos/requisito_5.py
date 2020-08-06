import numpy as np
from configuracion.listas import porcentajes


def validar_requisito_5(obj, ):
    """Procedimiento de clase para verificar cumplimiento de requisito 5 (% invertido en I+D)
    recibe self desde la clase
    validar_requisito_5(self, )"""
    try:
        dividir = (float(obj.lineEdit_3.text()) / float(obj.input_facturacion.text())) * 100
        dividir = np.round(dividir, 3)
        if obj.combo_tipo_empresa.currentText() == porcentajes[0][0]:
            if dividir >= porcentajes[0][2]:
                obj.verificacion['requisito_5'] = 'Cumple'
            else:
                obj.verificacion['requisito_5'] = 'No Cumple'
        elif obj.combo_tipo_empresa.currentText() == porcentajes[1][0]:
            if dividir >= porcentajes[1][2]:
                obj.verificacion['requisito_5'] = 'Cumple'
            else:
                obj.verificacion['requisito_5'] = 'No Cumple'
        elif obj.combo_tipo_empresa.currentText() == porcentajes[2][0]:
            if dividir >= porcentajes[2][2]:
                obj.verificacion['requisito_5'] = 'Cumple'
            else:
                obj.verificacion['requisito_5'] = 'No Cumple'
        else:
            obj.verificacion['requisito_5'] = 'No se identifico el tipo de empresa'
    except Exception as e:
        print(e)
