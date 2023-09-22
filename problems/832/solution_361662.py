def eh_quadrada(matriz):
    '''A função recebe uma matriz, conta a quantidade de linhas e colunas e retorna,
        compara as quantidades e retorna o resultado se o parametro de entrada é
        uma matriz quadrada ou não;
        list --> bool
    '''
    linhas = len(matriz)
    colunas = len(matriz[0])

    if linhas == colunas or matriz==[]:
        return True
    
    else:
        return False