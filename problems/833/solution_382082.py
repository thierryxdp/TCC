def conta_numero(numero,matriz):
    m=len(matriz)
    n=len(matriz[0])
    cont=0
    for i in range(m):
        for j in range(n):
            if cont_horizontal(numero,matriz,i,j):
                cont=cont+1
            if cont_vertical(numero,matriz,i,j):
                cont=cont+1
            
    return contador