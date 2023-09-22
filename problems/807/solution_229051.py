def conta_frases(texto):
'''Retorna o número de frases presentes no texto
dado. 

str -> int'''
    
    texto1=str.join('*',str.split(texto,'...')) 

	return str.count(texto1,'.')+str.count(texto1,'?')+str.count(texto1,'!')+str.count(texto1,'*')