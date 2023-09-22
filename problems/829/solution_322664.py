def soma_h(N):
    lista = 0
    for numero in range(N):
        lista = lista + round(1/N, 2)
    return sum(lista)