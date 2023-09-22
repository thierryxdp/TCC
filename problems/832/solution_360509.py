def eh_quadrada (matriz):
    """ A função eh_quadrada identifica se uma matriz é quadrada. 
    Obs: uma matriz vazia (sem nenhuma linha nem coluna) é considerada quadrada.
    list --> bool"""
    if len(matriz) == 0:
        return True
    else:
        return len(matriz) == len(matriz[0])

print (eh_quadrada ([[1,2],[3,4]]), eh_quadrada ([]), eh_quadrada ([[1,2]]), eh_quadrada ([[1],[2]]))