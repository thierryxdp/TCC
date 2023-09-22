def uppCons(frase):
	'''
    str->str'''
	transform_lista=list(frase)
	contador=0
	quantidade_letras=len(transform_lista)
	while (contador<quantidade_letras):
		if transform_lista[contador]!= "a" and transform_lista[contador]!="e" and transform_lista[contador]!="i" and transform_lista[contador]!="o" and transform_lista[contador]!="u" and transform_lista[contador]!=" " :
			transform_lista[contador].upper()
	contador=contador+1
    resultado=" ".join(transform_lista)
	return resultado