'''Funçao que recebe um texto e substitui todas as pontuações
	apresentadas nele por espaços. O texto deve, obrigatoriamente,
    ser inserido entre aspas.
    str -> str'''
def retira_pontuacao(texto):
    for pontuacao in '.!?-,:;':
        texto=texto.replace(pontuacao, ' ')
    return texto