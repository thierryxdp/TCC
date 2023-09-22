def conta_frases(x):
    "A função retorna a quantidade de frases de um texto. str -> str"
    
    y = ['.','!','?']
    i = 0
    z = 0
    v = 0
    
    while len(x) > i:
        if x[i] in y and x[i] != x[i+1]:
            z = z + 1
        i = i + 1
        
    return z