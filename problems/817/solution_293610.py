def acima_da_media(lista):
    '''retorna lista com notas acima da media'''
    soma = 0
    for x in range(len(lista)):
		soma += lista[x]
	media = soma / len(lista)
    
    lista2 = []
    for x in range(len(lista)):
       	if(lista[x] > media):
            lista2.append(lista[x])
    
    lista2.sort()
    return lista2