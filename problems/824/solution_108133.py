def uppCons(frase):
	'''
    str->str'''
	transform_lista=list(frase)
	contador=0
	quantidade_letras=len(transform_lista)
	while (contador<quantidade_letras):
		if transform_lista[contador]!= "a" and trasnform_lista[contador]!="e" and trasnform_lista[contador]!="i" and trasnform_lista[contador]!="o" and trasnform_lista[contador]!="u" and trasnform_lista[contador]!=" " :
			tranform_lista[contador].upper()
	contador=contador+1
    resultado=" ".join(transform_lista)
	return resultado