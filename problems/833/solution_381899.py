def conta_numero(numero,matriz):
    '''retorna quatas vezes um dado número aparece na matriz'''
    cont=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                cont=cont+1
    return cont