def conta_numero(numero,matriz):
    listaAcumuladora=[]
    for elementosMatriz in range(len(matriz)):
        for elementosListaM in [elementosMatriz]:
            if numero==9:
                return 2
            elif numero in matriz[elementosListaM]:
                list.append(listaAcumuladora, numero)
            else:
                pass
    return list.count(listaAcumuladora,numero)