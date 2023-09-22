def conta_numero(n,matriz):
    i=0
    repeticoes=0
    
    while i < len(matriz):
        if n in matriz:
            repeticoes=repeticoes+1
            i=i+1
    return repeticoes