def conta_numero(n,matriz):
    i=0
    repeticoes=0
    
    for i in range(len(matriz)):
        if n in matriz:
            repeticoes=repeticoes+1
    return repeticoes