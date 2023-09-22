def colchao(medidas,H,L):
    '''Funçao que dada a altura e largura de uma porta e as medidas de um
    colchao(lista) diz se ele vai se chocar ou nao com a porta'''
    if medidas[1] <= H:
        return True
    elif medidas[2] <= H:
        return True