def soma_h(N):
    lista = []
    for i in range(1, (N  + 1)):
        lista.append(1/i)
    return round(sum(lista),2)