def retira_pontuacao(x):
    """retira as pontuacoes de uma frase
    x->frase
    str->str"""
    pontuacao='!' and '-' and ',' and ':' and ';' and '.'
    return str.replace(x,pontuacao,' ')