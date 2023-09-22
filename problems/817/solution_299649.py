def maiores(lista_numeros, n):
    """Função que, dada uma lista de números inteiros
    e um número inteiro n, retorna outra lista que contenha
    todos os números da lista original maiores que n,
    ordenados em ordem crescente.
    list , int -> list"""
    lista = [n]
    lista1 = lista_numeros + lista
    list.sort(lista1)
    return lista1[(list.index(lista1, n)+1):]

def acima_da_media(lista_notas, media):
    """"""
    return list.sort(maiores(lista_notas, media))