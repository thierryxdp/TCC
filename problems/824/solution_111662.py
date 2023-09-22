def uppConst(frase):
    """ Dada uma frase, itera por meio dela e
    concatena cada consoante a uma frase em maíusculo, e as outras da forma que estão,
    ao final da iteração, retorna a frase com todas as consoantes em maíusculo.
    str -> str
    """
    i = 0
    tamanhoFrase = len(frase)
    fraseNova = ''
    while i < tamanhoFrase:
        if(not frase[i].lower() in 'aeiou'):
            fraseNova += frase[i].upper()
        else:
            fraseNova += frase[i]
        i += 1
    return fraseNova