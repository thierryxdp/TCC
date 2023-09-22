def retira_pontuacao(frase):
    '''
    	Função que recebe uma frase e retorna a frase substituindo toda pontuação por ' '
        str ->str
    '''
    frase = frase.replace('-', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    return frase