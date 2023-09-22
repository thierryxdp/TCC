def conta_numero(numero,matriz):
    '''funçao que dado um numero inteiro e uma matriz de tamanho qualquer
    ,conta e retorna quantas vezes o numero aparece na matriz'''
    contador = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if numero == matriz[i][j]:
                contador +=1
            else:
                pass
    return contador