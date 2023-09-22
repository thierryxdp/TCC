def inverte(frase):
	'''inverte a ordem das palavras de uma frase, tira suas pontuações e deixa tudo em letras minúsculas
   	str -> str'''
    palavras = str.split(frase,' ')
    str.replace(frase,',',' ').replace('.',' ').replace('-',' ').replace('!',' ').replace('?',' ')	
    return palavras´[::-1]