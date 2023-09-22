def soma_h(N):
    resultado = 0
    for i in list(range(1,N)):
        resultado = resultado + (1/i)
    return round(resultado,2)