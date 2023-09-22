def eh_quadrada(matriz):
    '''funcao que dada uma matriz,retorna true se ela for quadrada;
    list(list(int))-->bool'''
    if len(matriz)==0:
        return True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if len(matriz[i])==len(matriz[i][j]):
                return True
            else:
                return False