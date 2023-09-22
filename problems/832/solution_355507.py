def eh_quadrada(matriz):
    '''Função que, dada uma matriz, diz se ela é quadrada ou não.
    list --> bool'''
    colunas = 0
    linhas = 0
    for x in matriz:
        linhas = linhas + 1
        for y in x:
            colunas = colunas + (1/len(matriz))
    if linhas == colunas:
        return True
    else:
        return False