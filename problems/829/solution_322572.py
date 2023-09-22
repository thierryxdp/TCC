def soma_h(numero):
    i = 1
    lista = []
    while i < numero:
        lista = lista + [1/i]
        i = i + 1
    return round(sum(lista),2)