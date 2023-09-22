def conta_numero(numero,matriz):
    ls=[]
    l=len(matriz)
    if matriz == ls:
        return 0
    for i in range(l):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                ls.append(numero)
    return len(ls)