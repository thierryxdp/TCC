def faltante(L):
    list.sort(lista)
    contador = 1
    anterior = lista[contador - 1]
    proximo = lista[contador]
    while contador <= len(lista) and proximo == anterior + 1:
        contador = contador + 1
        anterior = lista[contador - 1]
        proximo = lista[contador]
    return anterior + 1