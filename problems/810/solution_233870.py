def inverte(frase):
	'''dada uma frase, retorna outra com as palavras na ordem inversa'''
    lista_palavras =str.split(frase,' ')
    lista_invertida =lista_palavras[::-1]
    f_contrário =str.join(' ',lista_invertida)
	return str.replace(str.replace(str.replace(str.replace(str.lower(f_contrário),',',''),'.',''),'!',''),'?','')