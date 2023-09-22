def conta_numero(numero,matriz):
    '''
    Funcao que tem como entrada um numero inteiro e uma
    matriz e retorna quantas vezes o numero que foi dado 
    aparece na matriz.
        Parametros:
            entrada:
                numero, matriz: int,list
            saida:
                int
    '''
    a = []
    b = len(matriz)
    for i in range(b):
        a.append(matriz[i].count(numero))
    return sum(a)