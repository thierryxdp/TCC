def conta_numero(numero,matriz):
    a=[]
    for l in matriz:
        for numero in l:
            if matriz[l]==numero:
                a.append(numero)
    return len(a)