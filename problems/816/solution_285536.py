def insere(lista_numero,n):
    '''Função que insere o número n na lista lista_numero de modo que ela fique ordenada de forma crescente
	lista, int -> lista'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    '''Função que dada uma lista e um número, retorna ima lista com apenas os números maiores que o número fornecido
    lista, float -> lista'''
    list.sort(lista)
    insere(lista,n)
    str.split(lista,n)