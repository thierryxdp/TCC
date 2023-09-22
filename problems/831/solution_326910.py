def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	palavra = palavra.lower()
    i = 0
    while i < len(palavra):
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            palavra[i.index+1] += "p" + palavra[i.index]
        i += 1 
    return palavra