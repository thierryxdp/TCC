def uppCons(frase):
    """ Funcao que retorna todas as consoantes em maiusculas
    str->str"""
    stringNova = ''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxyzç':
            stringNova = stringNova + frase[contador].upper()
    	else:
            stringNova = stringNova + frase[contador]
    	contador += 1
	return stringNova