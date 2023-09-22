def soma_h(n):
    resultado = 0
    for denominador in range(n, 0, -1):
        resultado += 1.0/denominador
    
    return round(resultado, 2)