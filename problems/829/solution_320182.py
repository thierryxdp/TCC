def soma_h(n):
    acumulador = 0
    for num in range(n):
        acumulador += 1/float(num+1)
        print(acumulador)
    acumulador=round(n,2)
    return acumulador