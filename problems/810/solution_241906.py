def inverte(texto):
    '''
    Dado um texto inverte a ordem das palavras o texto devidamente invertido e sem nenhum sinal de pontuação; string -> string'''
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d