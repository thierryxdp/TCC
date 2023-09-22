def maiores(lista, numero):
    """Dada uma lista e um número, está função retorna uma nova lista com todos os elementos
    da primeira lista que sejam maiores do que um determinado número.
       Onde: "lista" - lista inicial com diversos números;
             "numero" - número que servirá de parametro.
    list, int -> list"""
    lista.append(numero)
    lista.sort()
    indice = lista.index(numero)
    if lista.count(numero) == 1:
        return lista[indice + 1:]
    elif lista.count(numero) > 1:
        return lista[indice + lista.count(numero):]

def acima_da_media(notas):
    """ """
    media  = sum(notas) / len(notas)
    notas_acima_media = maiores(notas, media)
    return notas_acima_media