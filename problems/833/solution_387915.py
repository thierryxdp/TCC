def conta_numero(numero, matriz):
    '''
    Funcao que recebe um numero inteiro e uma matriz.
    A funcao conta e retorna quantas vezes aquele numero
    aparece na matriz.
    int, list -> int
    '''    
    con = 0
    for i in range(len(matriz)):
        lista_linha =  matriz[i]
        for j in range(len(lista_linha)):
            num = matriz[i][j]
            if num == numero:
                con =+ 1
    return con