def conta_numero(numero,matriz):
    
    a=0
    
    for i in matriz:
        for j in matriz[i]:
            a+=matriz[j].count(numero)
    return  a