def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	codigo = palavra.lower()
    for i in codigo:
        if i in "aeiou":
            palavra[palavra.index(i)+1] = "p" + palavra[palavra.index(i)]
    return palavra