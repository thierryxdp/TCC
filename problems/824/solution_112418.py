def uppCons(frase):
    '''Dada uma frase como entrada, retorna a mesma
    com todas as consoantes em letra maiuscula
    str -> str'''
    contador = 0
    frase.upper()
    while contador < len(frase):
        if frase[contador] in 'AEIOUaeiou':
            frase[contador].lower()
		contador +=1
	return frase