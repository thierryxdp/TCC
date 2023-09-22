def repetidos(numeros):
    i=1
    con=0
    while i<=len(numeros)-1:
        if lista[i]==lista[i-1]:
            cont+=1
        i+=1
    return con