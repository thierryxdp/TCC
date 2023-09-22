def soma_h(numero):
    i = 1
    lista = []
    div = 1/i
    while i != numero:
        lista = lista + [div]
        i = i + 1
    return sum(lista)