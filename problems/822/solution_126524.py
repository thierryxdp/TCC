def repetidos(lista):
    i = 0
    rep = 0
    
	for n in lista:
        if n == lista[i]:
            rep = rep + 1
            i= i+1
        else:
            i = i + 1
    return rep