def insere(lista_numero,n):
    """função que retorna uma lista em ordem crescente
    lista, int -> lista"""
    lista = [lista_numero,] + [n,]
    return list.sort(lista)