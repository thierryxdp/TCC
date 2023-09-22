def uppCons(frase):
    """Esta função recebe uma string e torna as consoantes maiusculas
    str -> str"""
    frase = list(frase)
    for x in range(len(frase)):
        if frase[x] in "o show dos paralamas do sucesso foi muito bom!":
            frase[x] = frase[x].upper()
    frase = "".join(frase)
    return frase