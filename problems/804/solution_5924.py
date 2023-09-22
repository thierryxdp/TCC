def filtra_pares(t1):
    valor1 = len(t1)
    valor2 = len(t1)
    valor3 = len(t1)
    valor4 = len(t1)
    if valor1%2 == 0 and valor2%2 == 0:
        return valor1,valor2
    elif valor1%2 == 0 and valor3%2 == 0:
        return valor1, valor2
    elif valor1%2 == 0 and valor4%2 == 0:
        return valor1, valor2
    elif valor2%2 == 0 and valor3%2 == 0:
        return valor2, valor3
    elif valor2%2 == 0 and valor4%2 == 0:
        return valor2, valor4
    elif valor3%2 == 0 and valor4%2 == 0:
        return valor3,valor4
    elif valor1%2 == 0:
        return valor1
    elif valor2%2 == 0:
        return valor2
    elif valor3%2 == 0:
        return valor3
    else:
        return valor4