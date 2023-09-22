def conta_numero(numero,matriz):
    """ Funcao que recebe um inteiro "numero" e uma lista "matriz"
    e retorna a quantidade de vezes que o inteiro "numero" é 
    encontrado na lista "matriz" """
    """ int, list -> int """
    somatorio=0
    for linha in range(0,len(matriz)):
        for coluna in range(0,len(matriz)):
            if matriz[linha][coluna]==numero
            somatorio +=1
    return somatorio
#casos de teste:
""" conta_numero(2,[[2,2,2],[1,2,1],[3,3,3]])
>>> 4
    conta_numero(3,[[3,3],[3,3],[3,3],[3,3]])
>>> 8
    conta_numero(4,[[2,2,1],[1,1,1],[1,2,3]])
>>> 0 """