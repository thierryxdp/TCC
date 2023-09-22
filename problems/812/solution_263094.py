def retira_pontuacao(frase):
    """Tem como objetivo receber uma frase e retornar
    essa mesma frase sem as pontuações.
    str > str"""
    punct = frase.punctuation
    for c in punct:
        frase = frase.replace(c, "")
    return frase