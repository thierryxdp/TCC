def conta_numero(numero,matriz):
    a=[]
    for i in range(len(matriz)):
        a.append(matriz.count(numero))
    return sum(a)