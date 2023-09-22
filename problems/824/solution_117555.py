def uppCons(frase):
    '''Recebe como entrada uma frase e retorna a 
    a frase com suas consoantes em maiúsculas.
    string -> string'''
    x = 0
    l_frase = list(frase)
    while x < len(frase):
    	if 'a'or'e'or'i'or'o'or'u'or'A'or'E'or'I'or'O'or'U' not in frase:
        	a = frase[x].upper()
        return frase[x].upper()
		x += 1