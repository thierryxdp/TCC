def uppCons(frase):
    """função que dada uma frase, retorna a mesma frase com todas as consoantes em maiúsculas
	str -> str"""
    
    consoantes = 'bcdfghjklmnpqrstvxwyz'
    s = ''
    
    for letra in frase:
        if letra in consoantes:
            s += letra.upper()
        else:
            s += letra
	return s