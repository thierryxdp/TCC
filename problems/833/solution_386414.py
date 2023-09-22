def conta_numero(numero,matriz):
    '''função que calcula quantas vezes um numero aparece na matriz
    	int, list --> int'''
    conta = 0
    for linha in matriz:
        for valor in linha:
            if valor == numero:
                conta = conta + 1
    return conta