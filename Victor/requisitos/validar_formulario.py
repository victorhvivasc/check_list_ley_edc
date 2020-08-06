from requisitos import requisito_1, requisito_2, requisito_3, requisito_4, requisito_5, requisito_6


def validar_formulario(obj, ):
    requisito_1.validar_requisito_1(obj, )
    requisito_2.validar_requisito_2(obj, )
    requisito_3.validar_requisito_3(obj, )
    requisito_4.validar_requisito_4(obj, )
    requisito_5.validar_requisito_5(obj, )
    requisito_6.validar_requisito_6(obj, )
    cumple = ''
    no_cumple = ''
    for x in obj.verificacion:
        if obj.verificacion[x] == 'Cumple':
            cumple += ' ' + x
        else:
            no_cumple += ' ' + x
    nombre, cuit = obj.input_nombre_empresa.text(), obj.input_cuit.text()
    tipo, activ = obj.combo_tipo_empresa.currentText(), obj.combo_actividades.currentText()
    r1, r2 = obj.porcentaje_asignado.text(), obj.verificacion['requisito_2']
    r3, r4 = obj.comboBox.currentText(), obj.lineEdit.text()
    r5, r6 = obj.lineEdit_3.text(), obj.lineEdit_4.text()
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
    texto1 = texto + '\n\n' + "Cumple los requisitos: " + str(cumple) + '\n' + "No " \
        "Cumple los requisitos: " + str(no_cumple) + '\n'
    return texto1, cuit
