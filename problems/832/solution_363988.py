def eh_quadrada(matriz):
    '''
    Funcao que recebe uma matriz, e
    retorna se essa matriz é quadrada ou nao.
    list -> bool
    '''
    linhas = len(matriz)
    if linhas>0:
        colunas = len(matriz[0])
        for i in range(1,len(matriz)):
            colunas2 = len(matriz[i])
            if colunas == colunas2:
                colunas = colunas2
            else:
                colunas = -1              
    else:
        colunas = 0
        
    if linhas == colunas:
        return True
    else:
        return False