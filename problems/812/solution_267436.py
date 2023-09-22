def retira_pontuacao(texto):
    """
    """
    f=texto
    punct = string.punctuation
    for c in punct:
        f = f.replace(c, "")
    return f