def conta_numero(numero, matriz):
    """ função que retorna o numero de vezes que um numero aparece na matriz """
    qtdNum = 0
    for linha in matriz:
    	qtdNum += list.count(linha, numero)
    return qtdNum