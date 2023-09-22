def conta_numero(numero,matriz):
    contador = 0
    for i in range(len(matriz)):
        contador = contador + list.count(matriz[i],numero)
    return contador