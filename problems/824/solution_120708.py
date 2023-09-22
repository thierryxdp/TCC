def uppCos(frase):
'''funcao que recebe uma frase como entrada e retorna a frase com todas as suas consoantes 
em maiusculo
str-->str'''
	i=0
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
        str.upper(frase[i])
        i=i+1
    return frase