def conta_numero(numero,matriz):
    """ """
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
        qtd = str.count(numero,matriz)
            total = total + qtd
        return total