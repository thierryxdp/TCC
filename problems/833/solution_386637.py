def conta_numero(numero,matriz):
    nlin=0
    
    nvezes=0
    while nlin < len(matriz):
        nvezes= nvezes + list.count(matriz[nlin],numero)
        
        nlin += 1
    return  nvezes