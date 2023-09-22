def conta_numero(numero,matriz):
    """Dado um número inteiro e uma matriz, conta e retorna quantas 
    vezes aquele número aparece na matriz
    int, list-->int"""
    for linha in matriz:
        contagem=0
        v=len(matriz[0])
        while i in range (v):
            if numero==linha[i]:
                contagem=contagem+1
    return contagem