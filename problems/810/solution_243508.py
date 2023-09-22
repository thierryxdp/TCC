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

def inverte (frase):
    '''
    	Função que inverte as palavras de uma frase, sem letrar maiúsculas e pontuação
        str -> str
    '''
    frase=retira_pontuacao(frase.lower())
    return frase.reverse()