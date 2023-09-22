def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	palavra = palavra.lower()
    i = 0
    while i < len(palavra):
        if palavra[i] == "a" or palavra[i] == "e" or palavra[i] == "i" or palavra[i] == "o" or palavra[i] == "u":
            palavra[palavra[i+1]] = "p" + palavra[palavra[i]]
        i += 1 
    return palavra