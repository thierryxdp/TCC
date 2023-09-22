def conta_numero(numero,matriz):
    """ """
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero in matriz:
                
                total = total + str.count(matriz,numero)
            return total