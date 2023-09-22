def uppCons(frase):
	'''
	str->str'''
	transform_lista=list(frase)
	contador=0
	quantidade_letras=len(transform_lista)
	while (contador<quantidade_letras):
		if transform_lista[0][contador]!= "a" and transform_lista[0][contador]!="e" and transform_lista[0][contador]!="i" and transform_lista[0][contador]!="o" and transform_lista[0][contador]!="u" and transform_lista[0][contador]!=" " :
			transform_lista[0][contador].upper
		contador=contador+1
    resultado="".join(transform_lista)
	return resultado