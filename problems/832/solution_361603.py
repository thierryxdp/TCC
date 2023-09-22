def eh_quadrada(matriz):
    '''A função recebe uma matriz, conta a quantidade de linhas e colunas e retorna,
        compara as quantidades e retorna o resultado se o parametro de entrada é
        uma matriz quadrada ou não;
        list --> str
    '''
    linhas = len(matriz)
    colunas = len(matriz[0])

    if linhas == colunas or linhas and colunas == 0:
        return True
    if linhas ==0 and colunas ==0:
        return True
    else:
        return False