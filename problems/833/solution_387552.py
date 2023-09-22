def conta_numero(numero,matriz):
    
    a=0
    
    for i in matriz:
        for j in matriz:
            a+=matriz[j].count(numero)
    return  a