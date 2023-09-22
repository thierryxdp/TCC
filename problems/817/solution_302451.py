def maiores(lista_numeros, n):
    i = 0
    lista_atualizada = []
    while i < len(lista_numeros):
        if lista_numeros[i] > n:
        	lista_atualizada.append(lista_numeros[i])
        	i += 1
    		lista_atualizada.sort()
    return lista_atualizada

def acima_da_media(notas):
    i = 0
    x = 0
    while i < len(notas):
    	x += notas[i]
        i+=1
    	x = x/len(notas)
	return maiores(notas, x)