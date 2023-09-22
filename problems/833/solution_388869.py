def conta_numero(numero, matriz):
    cont=0
    n=len(matriz)-1
    while n>=0:
        for num in matriz[n]:
            if num == numero:
                cont=cont+1
        n=n-1
    return cont