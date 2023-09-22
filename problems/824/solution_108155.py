def uppCons(frase):
	'''
	str->str'''
	transform_lista=list(frase)
    lista_nova =[]
	lista_consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'] 
	contador=0
	quantidade_letras=len(transform_lista)
	while (contador<quantidade_letras):
		if transform_lista[contador] in lista_consoantes:
			alta = transform_lista[contador].upper()
			lista_nova.append(alta)
		else:
			lista_nova.append(transform_lista[contador])
		contador=contador+1
    resultado="".join(lista_nova)
	return resultado