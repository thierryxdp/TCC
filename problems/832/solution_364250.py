def eh_quadrada(matriz):
    '''
       Dada uma matriz retorna True se a matriz for quadrada
       ou retorna False se a matriz não for quadrada.
       list -> bool
    '''
    quadrada = True
    for i in range(len(matriz)):
        if i == 0:
            quadrada = True
        for j in range(len(matriz[0])):
            if i == j:
                quadrada = True
            if i != j:
                quadrada = False
    return quadrada