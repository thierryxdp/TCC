def conta_numero(numero, matriz):
    contador = 0
    for i in matriz:
        for j in matriz[0]:
            contador = list.count(matriz,numero)
            if contador == 1:
                qtd = contador + 1
    return qtd