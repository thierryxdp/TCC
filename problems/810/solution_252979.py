def retira_pontuacao(frase):
    """Substitui as pontuações por espaços"""
    ls = [("!", " "), ("-", " "), (",", " "), (":", " "), (";", " "), ("?", " "), ("...", " "), (".", " ")]
    for m in ls:
        frase = str.replace(frase, m[0], m[1])
    return frase
def inverte(frase):
    """Recebe uma frase e retorna a frase com a ordem das palavras invertida.
    assinatura: str -> str"""
    a = str.lower(frase)
    b = str.split(frase)
    c = frase[::-1]
    d = str.join(' ', frase)
    return a + b + c + d