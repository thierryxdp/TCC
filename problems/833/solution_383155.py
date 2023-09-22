def conta_numero(numero,matriz):
    contador = 0
    for i in matriz:
        indice = 0
        for j in matriz[indice]:
            if j == numero:
                contador +=1
            indice +=1
    return contador