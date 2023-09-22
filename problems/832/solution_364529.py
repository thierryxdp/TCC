def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada;
       list => Bool'''
    externo = []
    interno = []
    for i in matriz:
        externo.append(i)
        for e in i:
            interno.append(e)
    quant_ext = len(externo)
    quant_int = len(interno)
    
    if quant_ext == quant_int:
        return True
    if quant_ext != quant_int:
        return False