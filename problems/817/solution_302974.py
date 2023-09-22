def acima_da_media(notas):
    i = 0
    x = 0
    while i < len(notas):
    	x += notas[i]
        i+=1
    x = x/len(notas)
		return maiores(notas, x)