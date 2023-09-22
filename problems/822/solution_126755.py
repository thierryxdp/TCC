def repetidos(lista):
    repeticao = 0
    i = 0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            repeticao=repeticao+1
		i=i+1
	return repeticao