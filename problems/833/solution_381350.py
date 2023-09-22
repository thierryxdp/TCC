def conta_numero(numero,matriz):
    lista=[]
    for i in range(i+1):
        for j in matriz[i]:
            if numero in matriz[i]:
                lista=lista+[numero]
    
    return len(lista)