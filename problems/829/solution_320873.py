def soma_h(N):
    "Calcula o valor de H com N termos. int->float"
    denominador = range(1,N+1)
    H = 0
    N = range(1,N+1)
    for denominador in N:
        num = 1/denominador
        H += num
    return round(H, 2)