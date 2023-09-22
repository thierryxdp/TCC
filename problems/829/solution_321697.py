def soma_h(n):
    lista = []
    for i in range(1,n+1):
        lista.append(1/i)
    s = sum(lista)
    return round(s,2)