"""Recebe uma frase e retorna a mesma com todas as suas consoantes em maiúscula
str -> str"""

def uppCons(frase):
    i = 0 
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase.replace(frase[i], frase[i].upper())
        i = i + 1
	return frase