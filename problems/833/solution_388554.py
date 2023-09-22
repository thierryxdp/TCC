def conta_numero(numero,matriz):
    '''funçao que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, conta
    e retorna quantas vezes aquele numero aparece na matriz; int,list->int'''
    m=0
    for linha in matriz:
        m= m+list.count(linha,numero)
    return m