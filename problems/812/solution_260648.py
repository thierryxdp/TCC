def retira_pontuacao (frase):
    '''
    	essa função retira todos os sinais de pontuação da string recebida e os substitui
        por espaços
        str->str
    '''
    x = ('-,:;.')
    return frase.replace (x, "")