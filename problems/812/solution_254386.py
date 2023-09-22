def retira_pontuacao(f):
    import string
    pontuacao = f.maketrans('','',string.punctuation)
    for x in pontuacao:
        f = f.replace(x,' ')
    return f