def conta_numero(numero,matriz):
    """A função recebe um número inteiro e uma matriz de 
    inteiros de tamanho qualquer como entradas. Então conta,
    e retorna quantas vezes aquele número aparece na matriz.
    Entrada: Int,List
    Saída: Int"""
    
    soma=[]
    quantas=0
    for i in list(range(len(matriz))):
        soma += matriz[i]
        quantas=soma.count(numero)
    return quantas