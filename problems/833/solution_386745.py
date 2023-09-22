def conta_numero(numero,matriz):
    """Funão que, dado um número inteiro e uma matriz de 
    inteiros de tamanho qualquer, conta e retorna quantas
    vezes aquele número aparece na matriz.
    int,matriz->int"""
    quant=0
    for i in matriz:
        for j in i:
            if j==numero:
                quant+=1
    return quant