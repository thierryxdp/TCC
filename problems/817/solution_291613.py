def acima_da_media (lista):
	'''Forma uma lista com notas maiores que a média
Parâmetros: 
lista: list.
	lista que o usuario informou
Returns: list
uma lista com notas maiores que a média
	'''
    media = sum(lista) / len(lista)
    if media in lista:
        list.sort(lista)
        return lista[lista.index(media)+1:]
    else:
        lista.append(media)
        list.sort(lista)
        return lista[lista.index(media)+1:]