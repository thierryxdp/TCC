def repetidos (numeros):
    k=0
    x=0
    while k<len(numeros)-1:
        if numeros[k]==numeros[k+1]:
            x=x+1
        k=k+1
    return x