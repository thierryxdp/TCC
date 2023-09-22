def soma_h(n):
    lista = []
    for x in range(1, n+1):
        valor = 1/x
        lista.append(valor)
    return round(sum(lista), 2)