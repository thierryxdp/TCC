def conta_numero(numero,matriz):
    rep=[]
    proximo=0
    while proximo < len(matriz):
        if matriz[proximo] == numero:
            list.append(rep,matriz[proximo]) 
        proximo = proximo + 1
    return len(rep)