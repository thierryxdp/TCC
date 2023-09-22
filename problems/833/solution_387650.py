def conta_numero(numero,matriz):
    '''Retorna quantas vezes aquele número aparece na matriz.
    int,list -->int'''
    v=0
    for i in matriz:
        for j in i:
            if numero == j:
           		v +=1
    return v