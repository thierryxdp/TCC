def repetidos(x):
    i=0
    contador=0
    while i < len(x):
        if x[i] == x[i-1]:
            contador = contador + 1
        else:
            contador = contador
        i = i + 1 
    
    return contador