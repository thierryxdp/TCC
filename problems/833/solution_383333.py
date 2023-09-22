def conta_numero(numero,matriz):
    listaAcumuladora=[]
    for elementosMatriz in range(len(matriz)):
        for elementosListaM in range(len(elementosMatriz)):
            if numero in matriz[elementosListaM]:
                list.append(listaAcumuladora, numero)
            else:
                pass
    return listaAcumuladora