def soma_h(x):
    lista = [1,]
    for y in range(2, x + 1):
        fracao = 1/y
        lista.append(fracao)
    return round(sum(lista), 2)