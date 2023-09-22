def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	palavra = palavra.lower()
    for i in palavra:
        if i == "a":
            palavra[palavra.find("a")+1] = "pa"
        if i == "e":
            palavra[palavra.find("e")+1] = "pe"
        if i == "i":
            palavra[palavra.find("i")+1] = "pi"
        if i == "o":
            palavra[palavra.find("o")+1] = "po"
        if i == "u":
            palavra[palavra.find("u")+1] = "pu"
    return palavra