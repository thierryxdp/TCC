def conta_numero(numero,matriz):
    """A função recebe um número inteiro e uma matriz de 
    inteiros de tamanho qualquer como entradas. Então conta,
    e retorna quantas vezes aquele número aparece na matriz.
    Entrada: Int,List
    Saída: Int"""
    
    linha=((len(matriz))+1)
    for i in list(range(linha):
        for j in range(len(matriz[i])):
            matrize=matriz[i]
            quantas=matrize.count(numero)
    return quantas