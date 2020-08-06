def validar_requisito_1(obj, ):
    """Procedimiento de clase para verificar cumplimiento de requisito 1 (70% de facturacion)
    recibe self desde la clase
    validar_requisito_1(self, )"""
    try:
        division = (float(obj.lineEdit_2.text()) / float(obj.input_facturacion.text())) * 100
        obj.porcentaje_asignado.setText(str(division))
        if division >= 70:
            obj.verificacion['requisito_1'] = 'Cumple'
        else:
            obj.verificacion['requisito_1'] = 'No Cumple'
    except Exception as e:
        obj.verificacion['requisito_1'] = 'No indicado'
        print(e)
