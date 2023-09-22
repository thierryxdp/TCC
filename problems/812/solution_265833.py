def retira_pontuacao(texto):
    '''retira a pontuacao de um texto str->str'''
    return str.replace(texto,'.', ' ') and str.replace(texto,',', ' ') and str.replace(texto,'?', ' ')