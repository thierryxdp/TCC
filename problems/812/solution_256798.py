def retira_pontuacao(frase):
    
    '''Função que irá substituir quaisquer pontuação da frase por um espaço'''
    
    import string
    return frase.translate(string.maketrans("" ""),string.punctuation)