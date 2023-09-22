def uppCons(frase):
    ''' Dada como entrada uma frase, retorna a frase com 
    todas as suas consoantes em maiusculas
    str -> str'''
    contador = 0
    frase.upper()
    frase_nova = frase[0::]
    while contador < len(frase):
        if frase[contador] in 'AEIOU':
            frase[contador].lower()
		contador +=1
	return frase_nova