def conta_numero(numero,matriz):
    i=0
    j=0
    result=0
    while i<len(matriz):
        while j<len(matriz[0]):
            if numero==matriz[i][j]:
                result+=1
            j=j+1
        i=i+1
        j=0
    return result