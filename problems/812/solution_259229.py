def retira_pontuacao(x):
    """retira as pontuacoes de uma frase
    x->frase
    str->str"""
    if '!' in x:
        return str.replace(x,'!',' ')