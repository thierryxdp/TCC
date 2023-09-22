def retira_pontuacao(frase):
    '''
    Função que recebe uma frase e a retorna sem pontuação.
	str -> str
    '''
    texto = frase.replace('!', ' ')
    texto = texto.replace('?', ' ')
    texto = texto.replace('...', ' ')
    texto = texto.replace('.', ' ')
    texto = texto.replace(',', ' ')
    texto = texto.replace('—', ' ')
    texto = texto.replace(':', ' ')
    texto = texto.replace(';', ' ')
    texto = texto.replace('-', ' ')
    texto = texto.split()
    return ' '.join(texto)