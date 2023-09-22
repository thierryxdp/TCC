def conta_numero(numero:int,matriz:list)->int:
    '''retorna a quantidade de vezes que o número dado como parâmetro 
    aparece na matriz'''
    contador = 0
    nlinhas = len(matriz)
    for i in range(nlinhas):
        if i == 0:
            return 0
        else:
            for j in range(matriz[0]):
                if matriz[i][j] == numero:
                    contador += 1
    return contador