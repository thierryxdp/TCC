def conta_numero(numero,matriz):
    a=len(matriz)
    b=len(matriz[0])
    s=0
    for c in range(a):
        for i in range(b):
            if i==numero:
                s+=1
    return s