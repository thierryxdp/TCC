def lingua_p(palavra):
    """Este programa recebe uma palavra e traduz ela para a língua do P
    str -> str"""
    palavra = palavra.lower()
    vogal = "aeiou"
    for vogal in palavra:
        posicao = "aeiou".index
        palavra[posicao+1] = "p" + palavra[posicao]
    return palavra