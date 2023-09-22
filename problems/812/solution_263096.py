def retira_pontuacao(frase):
    """Tem como objetivo receber uma frase e retornar
    essa mesma frase sem as pontuações.
    str > str"""
    exclude = set(frase.punctuation)
    frase = ''.join(ch for ch in s if ch not in exclude)
    return frase