def faltante(lista):
    list.sort(lista)
    contador = 1
    anterior = lista[contador - 1]
    proximo = lista[contador]
    while contador < len(lista) and proximo == anterior + 1:
        contador = contador + 1
        anterior = lista[contador - 1]
        proximo = lista[contador]
    if anterior + 1 == proximo - 1:
        return anterior + 1
    else:
        return lista[-1] + 1