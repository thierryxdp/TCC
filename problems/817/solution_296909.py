def maiores (lista, n):
    """ retorna uma lista com os numeros maiores que n em ordem crescente."""
    list.append (lista, n)
    list.sort(lista)
    list.index(lista, n)
    lista2 = lista[list.index(lista,n) + 1:]
    return lista2
def acima_da_media (notas):
    media = sum(notas)//len(notas)
    return media