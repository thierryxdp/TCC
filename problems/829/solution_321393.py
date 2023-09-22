def soma_h(n):
    resultado = 1
    for i in list(range(1,n)):
        resultado = resultado + (1/i)
    return round(resultado,2)