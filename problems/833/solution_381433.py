def conta_numero(numero,matriz):
    '''Função que conta quantas vezes o elemento numero aparece na matriz dada.
       int,list --> int'''
    quant = 0
    for linha in matriz:
        quant += list.count(linha,numero)
    return quant