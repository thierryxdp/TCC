def maiores(lista,n):
    '''A função recebe uma lista e um inteiro n, e retorna uma nova lista com todos 
    os elementos maiores que n na lista original; ordem crescente.
    	list , int -- > list'''
    
    lista.sort()
	if lista == []:
        return []
    if lista[0] < n:
        lista.remove(lista[0])
        return maiores(lista,n)
    return lista


def acima_da_media(lista_notas):
    '''A função recebe uma lista com notas de avaliações de certa turma,
    e retorna uma lista ordenada (crescente) com as notas que ficaram acima da média
    		list -- > list'''

    media_notas = sum(lista_notas)/len(lista_notas)
    acima = maiores(lista_notas,media_notas)
    return acima