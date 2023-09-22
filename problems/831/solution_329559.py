def lingua_p(palavra):
    """Função que retorna uma palavra na 'língua do p', str->str"""
    palavrap=''
    for x in palavra:
        if x not in 'AÂÁEÊÉIÍOÓÔÚUaáâeéêiíoóôuú':
            palavrap+= str(x)
        if x in 'AÂÁEÊÉIÍOÓÔÚUaáâeéêiíoóôuú':
            palavrap+= str(x) + 'p' + str(x)
    return palavrap