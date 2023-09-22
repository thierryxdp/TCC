from math import floor
def hashtag(s):
	'''
dada uma str 's' como entrada, retorna a mesma str, mas com
# adicionado no início, no meio e no final
dados de entrada: str
dados de retorno: str
	'''
    posicao = floor(len(s)/2)
    return '#' + s[:posicao] + '#' + s[posicao:] + '#'