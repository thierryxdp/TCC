def conta_numero(numero,matriz):
    """Dado um número inteiro e uma matriz, conta e retorna quantas 
    vezes aquele número aparece na matriz
    int, list-->int"""
    if len(matriz)==0:
        return 0
    contagem=0
    for linha in matriz:
        for n in linha:
            if numero==n:
                contagem+=1
    return contagem