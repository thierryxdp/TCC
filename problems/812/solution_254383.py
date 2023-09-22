def retira_pontuacao(f):
    import string
    pontuacao = str.maketrans('','',string.punctuation)
    for x in pontuacao:
        f = f.replace(x,' ')
    return f