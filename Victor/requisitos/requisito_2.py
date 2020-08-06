def validar_requisito_2(obj, ):
    """Procedimiento de clase para verificar cumplimiento de requisito 2 (medio de verificacion)
    recibe self desde la clase
    validar_requisito_2(self, )"""
    try:
        if obj.radio_presenta.isChecked():
            obj.verificacion['requisito_2'] = 'Cumple'
        else:
            obj.verificacion['requisito_2'] = 'No Cumple'
    except Exception as e:
        print(e)
