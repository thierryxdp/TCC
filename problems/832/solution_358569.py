def eh_quadrada(matriz):
    '''função que identifica se uma matriz é quadrada
    (matriz)=
    saida = '''
    linhas=len(matriz)
    colunas=len(matriz[0])
    return linhas==colunas
    if len(matriz)==0:
        return True
    else:
        return False