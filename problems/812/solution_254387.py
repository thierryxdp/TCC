def retira_pontuacao(f):
    import string
    from string import maketrans
    pontuacao = str.maketrans('','',string.punctuation)
    for x in pontuacao:
        f = f.replace(x,' ')
    return f