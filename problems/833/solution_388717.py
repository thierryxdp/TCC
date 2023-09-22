def conta_numero(numero, matriz):
    cont=0
    for j in matriz:
        for i in j:
            if i == numero:
                cont+=1