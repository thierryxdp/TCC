def retira_pontuacao(frase):
    """Substitui as pontuações por espaços"""
    ls = [("!", " "), ("-", " "), (",", " "), (":", " "), (";", " "), ("?", " "), ("...", " "), (".", " ")]
    for m in ls:
        frase = str.replace(frase, m[0], m[1])
    return frase
def inverte(frase):
    return frase[::-1]
     texto = inverte(frase)
    print texto