def conta_numero(numero,matriz):
    ''''''
    contador=0
    for i in range(0,len(matriz)):
        if matriz[i]==numero:
            contador+=list.count(matriz,numero)
            return contador