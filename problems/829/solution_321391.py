def soma_h(n):
    resultado = 0
    for i in list(range(n)):
        resultado = resultado + (1/i)
    return round(resultado,2)