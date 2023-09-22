def maiores(lista_notas, n):
	'''
    	Funcao que recebe uma lista de numeros inteiros e um
        numero inteiro n e retorna outra lista ordenados em
        ordem crescente
        list, int -> list
    '''
    if n in lista_numero:
        list.sort(lista_notas)
        lista_n = lista_notas[list.index(lista_notas, n) + 1:]
        return lista_n
    
    else:
        lista_notas.insert(-1, n)
        list.sort(lista_notas)
        lista_n = lista_notas[list.index(lista_notas, n) + 1:]
        return lista_n

def acima_da_media(lista_notas):
    '''
    	Funcao que recebe uma lista com as notas dos alunos 
        de uma turma e retorna uma lista ordenada com as 
        notas que ficaram acima da media
        list -> list
    '''
    media = sum(lista_notas)/len(lista_notas)
    return maiores(lista_notas, media)