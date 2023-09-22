def conta_numero(numero,matriz):
    ls=[]
    l=len(matriz)
    c=len(matriz[0])
    if matriz == ls:
        return 0
    for i in range(l):
        for j in range(c):
            if matriz[i][j] == numero:
                ls.append(numero)
    return len(ls)