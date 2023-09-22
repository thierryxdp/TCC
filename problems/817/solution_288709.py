def insere(lista_numero, n):
	'''
	Dada uma lista de numeros em ordem crescente, adiciona-se um numero nessa lista
	de forma que ela continue em ordem crescente.
    
	Entrada/Saida:
	list, float -> list
	'''
	lista_numero.append(n)
	return sorted(lista_numero)

def maiores(lista, n):
	'''
	Dado um numero n e uma lista devolve uma lista com os numeros maiores que n.
    
	Entrada/Saida:
	list, int -> list
    '''
	lista = insere(lista, n)
	index = lista.index(n)
    if (n == lista[index + 1]):
        index += 1
	return lista[index + 1:]


def acima_da_media(notas):
    media = sum(notas)/len(notas)
    return maiores(notas, media)