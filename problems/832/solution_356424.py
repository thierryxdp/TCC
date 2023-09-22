def eh_quadrada(matriz):
    '''funcao que retorna se a matriz é uma matriz quadrada
    list->bool'''
    resultado=''
    if matriz==[]:
        return True
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i!=j:
                resultado=False
            if i==j:
                resultado=True
    return resultado