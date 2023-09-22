def acima_da_media(lista, n=5):
    """ dado uma lista de números inteiros e o inteiro n, retorna outra lista com todos os números maiores que n ordenados em ordem crescente
    agora para um n fixo, igual a 5, caso não seja dada a média.
    n = média
    list, int -> list"""
    list.append (lista,n)
    list.sort(lista)
    indice = list.index (lista, n)
    lista = lista[indice:]
    return lista