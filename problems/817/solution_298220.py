def maiores(lista, n):
    """funcao que dada uma lista de numeros inteiros e um numero inteiro n retorna outra lista contendo todos os numeros originais maiores que n
	list, int -> list"""
    
    list.insert(lista, 0, n)
    list.sort(lista, reverse=True)
    
    ordenado = list.index(lista, n, 0)
    del lista[ordenado::]
    
    return lista[::-1]

def acima_da_media(lista):
    """funcao que recebe uma lista com notas e retorna outra lista ordenada com as notas que ficaram acima da media
	list -> list"""
    
    soma = sum(lista)/len(lista)
    notas = maiores(lista, soma)
    
    return notas