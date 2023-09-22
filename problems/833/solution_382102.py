def conta_numeros(numero,matriz):
    m=len(matriz)
    n=len(matriz[0])
    cont=0
    for i in range m:
        for j in range n:
            if numero==i:
                cont=cont+1
            if numero==j:
                cont=cont+1
    return cont