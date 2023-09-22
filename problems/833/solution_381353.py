def conta_numero(numero,matriz):
    lista=[]
    acumulador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero==matriz[i][j]:
                acumulador=acumulador+1
    
    return acumulador