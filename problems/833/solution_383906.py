def conta_numero(numero,matriz):
    a=[]
    for i in range(len(matriz)):
        a.append(a.count(numero))
    return sum(a)