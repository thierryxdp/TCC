def soma_h(n):
    resultado = 0
    for i in list(range(1,n+1)):
        resultado = resultado + (1/i)
    return round(resultado,2)