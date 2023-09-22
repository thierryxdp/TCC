def retira_pontuacao(frase):
    """Substitui as pontuações por espaços"""
    ls = [("!", " "), ("-", " "), (",", " "), (":", " "), (";", " "), ("?", " "), ("...", " "), (".", " ")]
    for m in ls:
        frase = str.replace(frase, m[0], m[1])
    return frase
def inverte(frase):
    lista = ["frase"]
    for m in lista:
        frase = list.reverse(frase)