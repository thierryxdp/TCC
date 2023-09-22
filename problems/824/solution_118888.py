def uppCons(frase):
'''Função que receba como entrada UMA frase e retorne a frase com todas as suas consoantes maiusculas '''
i=0
while i<len(frase):
    if frase[i]in 'bcdfghjklmnpqrstvxwyz':
        str.upper(frase[i])
    i=i+1
    return frase