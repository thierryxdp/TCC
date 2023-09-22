def soma_h(n):
    numero=1
    for i in range(1,n):
        numero += 1/i
    return round(numero,2)