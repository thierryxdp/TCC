def conta_numero(numero:int,matriz:list)->int:
    '''retorna a quantidade de vezes que o número dado como parâmetro 
    aparece na matriz'''
    contador = 0
    nlinhas = len(matriz)
    for i in range(nlinhas):
        for j in range len(matriz[0]):
            if matriz[i][j] == numero:
                contador += 1
    return contador