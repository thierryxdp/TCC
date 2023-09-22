def faltante(L):
    lista_organizada = list.sort(L)
    contador = 1
    anterior = lista_organizada[contador - 1]
    proximo = lista_organizada[contador]
    while proximo == anterior + 1:
        contador = contador + 1
    return anterior