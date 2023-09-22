def maiores(lista,n):
    """Função que dada uma lista de n° inteiros e um n inteiro n, retorna outra contendo
    todos os n° da lista original>n, ordenados em ordem crescente;
    list -> list"""
    list.append(lista, n)
    list.sort(lista)
    i = list.index(lista,n)
    return lista[i+1:]