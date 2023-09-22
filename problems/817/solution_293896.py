def maiores (lista, n):
	''' funcao que dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n;
lista , int -> lista '''
	list.append(lista, n)
	list.sort(lista)
	indice = list.index(lista, n)
	return lista[indice+list.count(n):]

def acima_da_media (lista, nota, media):
    ''' funcao que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da media;
lista -> lista '''
    media = sum(lista)/len(lista)
    lista_final = maiores(lista, media)
    return lista_final