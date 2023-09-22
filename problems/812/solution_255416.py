def retira_pontuacao(x):
	"""Função em que dada uma frase retorna a mesma onde todos os caracteres de pontuação (incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituídos por espaço.
	string ->> sring"""
	x=x.replace('.',' ')
	x=x.replace(',',' ')
	x=x.replace('/',' ')
	x=x.replace(':',' ')
	x=x.replace(';',' ')
    x=x.replace('!',' ')
    x=x.replace('?',' ')
	return x