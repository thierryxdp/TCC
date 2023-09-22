def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	palavra = palavra.lower()
    codigo =  ""
    i = 0
    while i < len(palavra):
        codigo += palavra[i]
    	i += 1
    return codigo