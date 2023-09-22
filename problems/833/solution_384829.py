def conta_numero(numero,matriz):
    ''' retorna quantas vezes um numero aparece na matriz
list, int -> int
'''
    contador=0
    for i in matriz:
        for k in i:
            if k==numero:
                contador+=1
    return contador