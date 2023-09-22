def retira_pontuacao(texto):
    '''retira a pontuacao de um texto str->str'''
    return str.replace(texto,'.', ' ', 1) and str.replace(texto,'!', ' ', 1)