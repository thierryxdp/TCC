def conta_numero(numero,matriz):
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero in matriz[i]:
                lista=lista+[numero]
    
    return len(lista)