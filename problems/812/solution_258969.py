def retira_pontuacao(x):
    """dada uma frase x, substitui todas as pontuacoes por espaco
    x->frase qualquer
    str->str"""
    out = s.translate(str.maketrans('', '', string.punctuation))
    print out