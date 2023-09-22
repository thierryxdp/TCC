def maiores(numeros, n):
    nova_lista = list.insert(numeros, 0, n)
    lista_ordem = list.sort(numeros)
    return lista_ordem[list.index(lista_ordem, n):]