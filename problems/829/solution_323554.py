def soma_h(n):
    resultado = 0
    for i in range(1,n):
        resultado += 1/i
        resultado = round(resultado,2)
    return resultado