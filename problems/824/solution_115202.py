def uppCons(frase):
	"""Recebe uma entrada e retorna as consoantes em letra 
    maiuscula int,int->int"""
    contador=0
    letra = 'bcdfghjklmnpqrstvxz'
    frase_final= ''
	while contador<len(frase):
			caractere = frase [contador]
			if caractere in letra:
    			caractere = str.upper(caractere)
    			frase_final+=caractere
				contador+=1
    return frase_final