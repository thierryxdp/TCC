def conta_numero(numero,matriz):
    '''Retorna quantas vezes aquele número aparece na matriz.
    int,list -->int'''
    v=0
    for i in matriz:
        if numero == i:
            vezes +=1
    return vezes