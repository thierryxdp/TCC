def retira_pontuacao(frase):
    """Substitui as pontuações por espaços"""
    ls = [("!", " "), ("-", " "), (",", " "), (":", " "), (";", " "), ("?", " "), ("...", " "), (".", " ")]
    for m in ls:
        frase = str.replace(frase, m[0], m[1])
    return frase
def inverte(frase):
    """Afunção recebe uma frase e a retorna sem as pontuações e letras maíusculas com a ordem das palavras invertida
    assinatura: str -> str"""
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.split(frase)
    frase = frase[::-1]
    frase = str.join[' ', frase]
    return frase