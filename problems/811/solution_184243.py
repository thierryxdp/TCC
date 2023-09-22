def colchao(medidas,H,L):
    '''Funçao que dada a altura e largura de uma porta e as medidas de um
    colchao(lista) diz se ele vai se chocar ou nao com a porta'''
    if medidas[1] > H:
        if medidas[2] > L:
            return True
        else:
            return False
  	if medidas[2] > H:
        if medidas[1] > L:
            return True
        else:
            return False