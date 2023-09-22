def conta_numero(matriz,n):
    """dado um numero inteiro e uma matriz de inteiros detamanho qualquer, conta e retorna quantas vezes aquele numero aparece na matriz"""
    qtd=0
    for i in matriz:
        qtd+=i.count(n)
    return qtd