def uppCons(frase):
    '''Dada como entrada uma frase, retorna a frase com
    todas suas consoantes em maiusculas.
    str -> str'''
    contador = 0
    while contador < len(frase):
        if frase[contador] not in 'AEIOUaeiou':
			frase[contador].upper()
		contador += 1
	return frase