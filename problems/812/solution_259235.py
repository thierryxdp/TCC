def retira_pontuacao(x):
    """retira as pontuacoes de uma frase
    x->frase
    str->str"""
    if len(x)=14:
        return str.replace(x,'!',' ')