def conta_numero(numero,matriz):
    '''funcao que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, conta
    e retorna quantas vezes quele numero aparece na matriz, list->int'''
    vezes=0
    for i in matriz:
        for m in i:
            if n==numero:
                vezes=vezes+1
    return vezes