def uppCons(frase):
    '''Dada como entrada uma frase, retorna a frase com
    todas suas consoantes em maiusculas.
    str -> str'''
    contador = 0
    frase_nova = frase.upper()
    while contador < len(frase):
        if frase_nova[contador] in 'AEIOU':
            frase_nova[contador].lower()
			return frase_nova