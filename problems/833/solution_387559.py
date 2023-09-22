def conta_numero(numero,matriz):
    
    a=0
    
    for i in matriz:
        a+=i.count(numero)
    return  a