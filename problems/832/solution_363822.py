def eh_quadrada(matriz):
    ''' função que define se uma matriz é quadrada.
    	uma matriz é quadrada quando o numero de linhas e de
        colunas é igual.
        list(list) ---> bool '''
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    elif linhas == 0 and colunas == 0:
        return True
    else:
        return False