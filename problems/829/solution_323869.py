def soma_h(n):
    i = 1
    numero = 0.0
    for i in range(1, n+1):
        numero = numero + 1/i;
    return round(numero,2)