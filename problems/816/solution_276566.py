def maiores(lista, n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista que contenha todos os numeros da lista original maiores que n
    lista de inteiro, int -> lista'''
    list.sort(lista)
    listanova = [lista] + [n]
    listanova = list.sort(listanova)
    list.split(listanova, ",")
    x = list.index(listanova, n)
    listaDois = listanova[x+1:]
    " ".join(listaDois)
    return listaDois