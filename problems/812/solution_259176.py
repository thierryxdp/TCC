def retira_pontuacao(frase):
    """substitui todos os caracteres de pontuacao de uma frase por espaco
    str->str"""
    out = ''.join([i for i in frase if i not in string.punctuation])
	print(out)