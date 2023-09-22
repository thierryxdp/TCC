def uppCons(frase):
    """Funcao que retorna a frase de entrada com
    todas as consoantes maiusculas"""
	str.upper(frase)
    proximo = 0
    while proximo < len(frase):
        if frase[proximo] in 'aeiou':
        	str.lower(frase[proximo])
        proximo = proximo + 1
	return frase