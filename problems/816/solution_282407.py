def maiores(lista, n):
    """tendo como parametros uma lista de números inteiros e um número inteiro, a função retorna outra lista, apenas com
    os elementos maiores que n. A lista retornada será em ordem crescente; list, int -> list"""
    listanova = lista + [n]
    list.sort (listanova)
    indexn = list.index(listanova, n)
    if lista[indexn] == lista[indexn+1] or lista[indexn] == lista[indexn-1]:
    	return: listanova[list.index(listanova,n]+list.count(listanova,n)::]
    else:
    	return listanova[indexn + 1::]