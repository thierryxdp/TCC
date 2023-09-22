def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	palavra = palavra.lower()
    palavra_p = ""
    i = 0
    for "a" in palavra:
        posicao = "a".index
        palavra[posicao+1] = "p" + palavra[posicao]
    for "e" in palavra:
        posicao = "e".index
        palavra[posicao+1] = "p" + palavra[posicao]
	for "i" in palavra:
        posicao = "i".index
        palavra[posicao+1] = "p" + palavra[posicao]
    for "o" in palavra:
        posicao = "o".index
        palavra[posicao+1] = "p" + palavra[posicao]
    for "u" in palavra:
        posicao = "u".index
        palavra[posicao+1] = "p" + palavra[posicao]
    return palavra