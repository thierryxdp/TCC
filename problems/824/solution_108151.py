def uppCons(frase):
	'''
	str->str'''
	transform_lista=list(frase)
    lista_nova =[]
	contador=0
	quantidade_letras=len(transform_lista)
	while (contador<quantidade_letras):
		if transform_lista[contador]!= "a" and transform_lista[contador]!="e" and transform_lista[contador]!="i" and transform_lista[contador]!="o" and transform_lista[contador]!="u" and transform_lista[contador]!=" " and transform_lista[contador]!="´" 
		and transform_lista[contador]!="~":
			alta = transform_lista[contador].upper()
			lista_nova.append(alta)
		else:
			lista_nova.append(transform_lista[contador])
		contador=contador+1
    resultado="".join(lista_nova)
	return resultado