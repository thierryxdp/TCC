def lingua_p(palavra):
    """Recebe uma palavra e retorna a mesma traduzida para a língua do P"""
    letras = tuple(palavra)
    palavra_p = ""
    for letras in palavra:
        if letras in "aeiouAEIOU":
            palavra_p += letras + "p" + letras
        if letras not in "aeiouAEIOU":
            palavra_p += letras
    return palavra_p