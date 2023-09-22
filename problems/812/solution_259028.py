def retira_pontuacao(frase):
    '''
    Função que rece uma frase e a retorna sem pontuação.
	str -> str
    '''
    texto = frase.replace('!', ' ').replace('?', ' ').replace('...', ' ').replace('.', ' ')
    texto = texto.replace(',', ' ').replace('—', ' ').replace(':', ' ').replace(';', ' ')
    return ' '.join(texto)