def soma_h(n):
    acumulador = 0
    for num in range(n):
        acumulador += 1/float(num+1)
        print round(num,2)
    return acumulador