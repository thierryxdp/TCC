def maiores(numeros, n):
    """Recebe uma lista e um número inteiro, e retorna uma lista com valores maiores que n.
    	List, int -> list"""
    maiores =[]
    numeros.sort()
    for i in range (0, len(numeros)):
        if numeros[i] > n:
            maiores.append(numeros[i])
    return maiores


def acima_da_media(lista):
    """Recebe uma lista com notas e retorna as maiores que a média da turma.
    	list -> list"""
	media = sum(lista)/len(lista)
    return maiores(lista, media)