def soma_h(n):
    lista = []
    comprimento = list(range(n + 1))[1:]
    for elemento in comprimento:
        lista = lista + [1/elemento]
    soma = sum(lista)
    return round(soma, 2)