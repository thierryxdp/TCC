def conta_numero(numero, matriz):
    """recebe um numero inteiro e uma matriz de inteiros e retorna a qauntidade
    de vezes que esse numero aparece na matriz
    int, list -> int"""
    
    lista = []
    
    for i in range(len(matriz)):
        lista += matriz[i]
        
    repeticoes = list.count(lista, numero)
    
    return repeticoes