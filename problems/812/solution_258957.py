def retira_pontuacao(x):
    """dada uma frase x, substitui todas as pontuacoes por espaco
    x->frase qualquer
    str->str"""
	if ('!' in x==True):
    return str.replace(x,'!',' ')