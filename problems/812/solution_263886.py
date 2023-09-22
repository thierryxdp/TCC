def retira_pontuacao(frase):
    '''função que retira toda a pontuação de uma frase sem exceção
    string -> string'''
    frase = str.replace('!', ' ')
    frase = str.replace('?', ' ')
    frase = str.replace('-', ' ')
    frase = str.replace('.', ' ')
    frase = str.replace(':', ' ')
    frase = str.replace(';', ' ')
    frase = str.replace(',', ' ')
    return frase