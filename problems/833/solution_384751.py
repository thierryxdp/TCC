def conta_numero(numero,matriz):
    """A função recebe um número inteiro e uma matriz de 
    inteiros de tamanho qualquer como entradas. Então conta,
    e retorna quantas vezes aquele número aparece na matriz.
    Entrada: Int,List
    Saída: Int"""
    
    for i in list(range(len(matriz))):
        if numero in matriz[i]:
        quantas=matriz[i].count(numero)
    return quantas