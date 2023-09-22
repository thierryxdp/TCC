def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	palavra = palavra.lower()
    codigo = ""
    i = 0
    while i < len(palavra):
        if palavra[i]== "a":
            palavra[i + 1] = "pa"
        if palavra[i]== "e":
            palavra[i + 1] = "pe"
        if palavra[i]== "i":
            palavra[i + 1] = "pi"
    	i += 1
	return palavra