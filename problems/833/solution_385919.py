def conta_numero(matriz,numero):
    '''Esta e a funcao que calcula quantas
vezes um dado numero aparece na matriz dada'''
    cont = 0
    for a in matriz:
        for b in a:
            if b == numero:
   		    cont += 1
    return cont