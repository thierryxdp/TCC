def soma_h(N):
    lista = 0
    for numero in range(1, N+1):
        lista = lista +1/numero
    return round(lista, 2)