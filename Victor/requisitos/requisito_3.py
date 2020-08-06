def validar_requisito_3(obj, ):
    """Procedimiento de clase para verificar cumplimiento de requisito 3 (mejora continua)
    recibe self desde la clase
    validar_requisito_3(self, )"""
    try:
        if obj.comboBox.currentText() == 'SÍ':
            obj.verificacion['requisito_3'] = 'Cumple'
        else:
            obj.verificacion['requisito_3'] = 'No Cumple'
    except Exception as e:
        obj.verificacion['requisito_3'] = 'No indicado'
        print(e)
