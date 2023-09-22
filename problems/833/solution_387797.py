def conta_numero( numero,matriz):
    ''' retorna quantas vezes aquele número aparece na matriz;
    entrada-> numero e matriz; int, list(mat)->list(list)'''
    c=0
    for linha in matriz:
        for elem in linha: 
            if elem == numero:
                c=c+1
    return c