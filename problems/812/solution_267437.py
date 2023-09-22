def retira_pontuacao(texto):
    """
    """
    f=texto
    punct = str.punctuation
    for c in punct:
        f = f.replace(c, "")
    return f