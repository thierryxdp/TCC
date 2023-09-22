def conta_numero(numero,matriz):
    ''''''
    
    a=list.count(matriz[0],numero)
    b=list.count(matriz[0][1],numero)
    
    if numero in len(matriz):
        return a