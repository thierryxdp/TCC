def conta_numero(numero,matriz):
    '''função que dada um numero e uma matriz conta e retorna quantas vezes aquele numero aparece na matriz;
    int,list->int'''
    rep = 0
    for lin in matriz:
        for elem in lin:
            if numero == elem:
                rep += 1
    return rep