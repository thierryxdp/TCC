def conta_numero(numero,matriz):
    
    a=0
    
    for i in matriz:
        a+=matriz[i].count(numero)
    return  a