def conta_numero( numero,matriz):
    ''' retorna quantas vezes aquele número aparece na matriz;
    entrada-> numero e matriz; int, list(mat)->list(list)'''
    c=0
    for elem in matriz:
        if elem == numero:
            c=c+1
    return c