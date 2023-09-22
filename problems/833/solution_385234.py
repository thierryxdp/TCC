def conta_numero(numero, matriz):
    num=0
    for i in matriz:
        for aij in i:
            if aij==numero:
                num=num+1
    return num