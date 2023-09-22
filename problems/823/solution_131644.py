def faltante(lista):
    lista_organizada = sort(lista)
    contador = 1
    anterior = lista_organizada[contador - 1]
    proximo = lista_organizada[contador]
    while proximo == anterior + 1:
        contador = contador + 1
    return anterior