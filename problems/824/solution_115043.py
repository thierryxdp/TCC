def uppCons(texto):
	i=0
	lista1=[]
	con=''
	while i<len(texto):
		if texto[i] in 'BCDFGHJKLMNPQRSTVWYZÇbcdfghjklmnpqrstvwyzç':
            con=con+texto[i]
            x=texto.upper()
            list.append(lista1,x[i])
		else:
            con=con+texto[i]
            x=texto.lower()
            list.append(lista1,x[i])
		i+=1
	if lista1[0] in 'aeiou':
            lista1[0] = lista1[0].upper()
	return ''.join(map(str, lista1))