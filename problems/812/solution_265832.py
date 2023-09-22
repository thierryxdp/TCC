def retira_pontuacao(texto):
    '''retira a pontuacao de um texto str->str'''
    return str.strip(texto,'.') and str.strip(texto,',') and str.strip(texto,'?')