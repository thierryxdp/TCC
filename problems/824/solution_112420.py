def uppCons(frase):
    '''Dada uma frase como entrada, retorna a mesma
    com todas as consoantes em letra maiuscula
    str -> str'''
    contador = 0
    x = frase[0::]
    x.upper()
    while contador < len(x):
        if x[contador] in 'AEIOUaeiou':
            x[contador].lower()
		contador +=1
	return x