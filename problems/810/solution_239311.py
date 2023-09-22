def inverte(frase):
	'''inverte a ordem das palavras de uma frase, tira suas pontuações e deixa tudo em letras minúsculas
   	str -> str'''
    str.replace(frase,',',' ').replace('.',' ').replace('-',' ').replace('!',' ').replace('?',' ')	
 	palavras = str.split(frase,' ')
    return palavras[-1:0]