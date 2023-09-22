def retira_pontuacao(frase):
    """Substitui as pontuações por espaços"""
    ls = [("!", " "), ("-", " "), (",", " "), (":", " "), (";", " "), ("?", " "), ("...", " "), (".", " ")]
    for m in ls:
        frase = str.replace(frase, m[0], m[1])
    return frase
def inverte(frase):
    """Recebe uma frase e retorna a frase com a ordem das palavras invertida.
    assinatura: str -> str"""
    frase = str.lower(frase)
    frase = str.split(frase)
    frase = frase[::-1]
    frase = str.join(' ', frase)
    return frase