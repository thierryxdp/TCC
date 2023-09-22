def conta_numero(numero,matriz):
    '''função que dado um número e uma matriz conta a quantidade de vezes que aquele aparece na matriz e faz uso dos laços aninhados'''
    cont= 0
    for l in matriz:
        for co in l:
            if co==numero:
                 cont= cont + 1
    return cont