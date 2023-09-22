def maiores(lista, numero):
    """Dada uma lista e um número, está função retorna uma nova lista com todos os elementos
    da primeira lista que sejam maiores do que um determinado número.
       Onde: "lista" - lista inicial com diversos números;
             "numero" - número que servirá de parametro.
    list, int -> list"""
    lista.append(numero)
    lista.sort()
    indice = lista.index(numero)
    return lista[indice + 1:]