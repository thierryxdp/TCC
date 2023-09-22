def filtra_pares(t1):
    valor1 = int(len(0))
    valor2 = int(len(1))
    valor3 = int(len(2))
    valor4 = int(len(3))
    if valor1%2 == 0 and valor2%2 == 0:
        return t1[valor1,valor2]
    elif valor1%2 == 0 and valor3%2 == 0:
        return t1[valor1, valor2]
    elif valor1%2 == 0 and valor4%2 == 0:
        return t1[valor1, valor2]
    elif valor2%2 == 0 and valor3%2 == 0:
        return t1[valor2, valor3]
    elif valor2%2 == 0 and valor4%2 == 0:
        return t1[valor2, valor4]
    elif valor3%2 == 0 and valor4%2 == 0:
        return t1[valor3,valor4]
    elif valor1%2 == 0:
        return t1[valor1]
    elif valor2%2 == 0:
        return t1[valor2]
    elif valor3%2 == 0:
        return t1[valor3]
    else:
        return t1[valor4]