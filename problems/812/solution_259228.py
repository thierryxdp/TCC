def retira_pontuacao(x):
    """retira as pontuacoes de uma frase
    x->frase
    str->str"""
    pontuacao=['!','-',',',':',';','.']
    return str.replace(x,pontuacao,' ')