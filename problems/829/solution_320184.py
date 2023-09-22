def soma_h(n):
    acumulador = 0
    for num in range(n):
        acumulador=round(n,2)
        acumulador += 1/float(num+1)
        print(acumulador)
    return acumulador