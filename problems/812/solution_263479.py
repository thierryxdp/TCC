def retira_pontuacao(text):
    '''Retorna o dado texto sem suas pontuações
    srt -> str'''
    return text.replace('...', ' ').replace('.', ' ').replace('-', ' ')
	.replace(';', ' ').replace('!', ' ').replace('?', ' ').replace(',', ' ')