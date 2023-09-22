def conta_numero(numero,matriz):
    """A função recebe um número inteiro e uma matriz de 
    inteiros de tamanho qualquer como entradas. Então conta,
    e retorna quantas vezes aquele número aparece na matriz.
    Entrada: Int,List
    Saída: Int"""
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            quantas=matriz.count(numero)
    return quantas