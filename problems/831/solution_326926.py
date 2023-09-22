def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	palavra = palavra.lower()
    codigo =  ""
    i = 0
    while i < len(palavra):
        codigo += palavra[i]
        if codigo[i] == "a":
            codigo["a".index + 1] = "pa"
        if codigo[i] == "e":
            codigo["e".index + 1] = "pe"
        if codigo[i] == "i":
            codigo["i".index + 1] = "pi"
        if codigo[i] == "o":
            codigo["o".index + 1] = "po"
        if codigo[i] == "u":
            codigo["u".index + 1] = "pu"
    	i += 1
    return codigo