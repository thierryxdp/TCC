def faltante(L):
    list.sort(L)
    contador = 1
    anterior = L[contador - 1]
    proximo = L[contador]
    while proximo == anterior + 1:
        contador = contador + 1
    return anterior