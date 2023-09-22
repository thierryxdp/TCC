def conta_numero(numero,matriz):
    """A função recebe um número inteiro e uma matriz de 
    inteiros de tamanho qualquer como entradas. Então conta,
    e retorna quantas vezes aquele número aparece na matriz.
    Entrada: Int,List
    Saída: Int"""
    
    soma=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            quantas=matriz[0][i].count(numero)
    return quantas