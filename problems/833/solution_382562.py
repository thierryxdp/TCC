def conta_numero(numero,matriz):
    l=list.count(matriz[3],numero)
    k=list.count(matriz[4],numero)
    for i in matriz:
        if numero in matriz[0]:
            return list.count(matriz[0],numero)
        if numero in matriz[1]:
            return list.count(matriz[1],numero)
        if numero in matriz[3]:
            return list.count(matriz[3],numero)
        if numero in matriz[4]:
            return list.count(matriz[4],numero)
        if numero in matriz[3] and matriz[4]:
            return l+k