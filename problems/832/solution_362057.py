def eh_quadrada(m):
    '''Função que, dada uma matriz de entrada, retorna se essa matriz é quadrada, ou seja, a quantidade de linhas é igual a quantidade de colunas; list [list] -> bool'''
    linhas=len(m)
    if linhas>0:
        colunas=len(m[0])
        if linhas==colunas:
            return True 
        else: 
            return False
    else:
        return True