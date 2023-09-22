'''Função que recebe uma lista de números inteiros com um novo
	elemento n e retorna uma nova lista a partir dele.
    list, int -> list'''
def maiores(lista,n):
    listaoriginal=lista[:]
    listaoriginal.append(n)
    listanova=listaoriginal[:]
    list.sort(listanova)
    listafinal=listanova[:]
    posicao=list.index(listafinal,n)+1
    return listafinal[posicao:]