def soma_h(n):
    cont = 0
    for h in range(1, n+1):
        cont = cont + 1/h
    return round(cont,2)