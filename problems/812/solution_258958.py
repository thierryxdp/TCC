def retira_pontuacao(x):
    """dada uma frase x, substitui todas as pontuacoes por espaco
    x->frase qualquer
    str->str"""
	if ('!' in x):
    return str.replace(x,'!',' ')