def maiores(lista_numeros, n):
    """função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contém todos os números da lista original maiores que n, ordenados em ordem crescente
    string -> string"""
    nova_lista = []
    list.sort(lista_numeros)
    for x in lista_numeros:
        if x > n:
            nova_lista.append(x)
    return nova_lista
def acima_da_media(lista_notas):
    nota = sum(lista_notas)/len(lista_notas)
    return maiores(lista,n)