def eh_quadrada(m):
    '''Função que, dada uma matriz de entrada, retorna se essa matriz é quadrada, ou seja, a quantidade de linhas é igual a quantidade de colunas; list [list] -> bool'''
    linhas=len(m)
    colunas=len(m[0])
    if linhas==colunas or m==[]:
        return True
    else:
        return False