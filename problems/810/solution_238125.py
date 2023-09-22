def inverte(frase):
	'''funcao q dada uma frase,retorna outra frase invertida com os seguintes detalhes:
	sem letras maiusculas e sem pontuacao'''
    a=retira_pontuacao(frase)
    b=str.lower(a)
    c=str.split(b,' ')
    d=c[::-1]
    e=str.join(' ',d)
    return e