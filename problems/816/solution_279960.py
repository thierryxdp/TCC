'''Função que recebe uma lista de números inteiros com um novo
	elemento n e retorna uma nova lista a partir dele.
    list, int -> list'''
def maiores(lista,n):
    lista=lista[:]
    listanova=lista.append(n)
    listaordenada=list.sort(lista[:])
    posicao=list.index(lista,n)+1
    return lista[posicao:]