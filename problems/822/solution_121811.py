def repetidos(numeros):
    i=1
    con=0
    while i<=len(numeros)-1:
        if numeros[i]==numeros[i-1]:
            con+=1
        i+=1
    return con