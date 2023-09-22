def maiores(lista_numeros,n):
    "retorna uma lista com números maiores que n ordenados em ordem crescente"
    "list, int -> list"
    filtrado=[element for element in lista_numeros if element > n]
    filtrado.sort()
	return filtrado

def acima_da_media(lista_numeros):
    "retorna uma lista ordenada com as notas dos alunos que ficaram acima da média"
    "list -> list"
    media=(sum(lista_numeros))/(len(lista_numeros))
    return maiores(lista_numeros,media)