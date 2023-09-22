def retira_pontuacao(frase):
    '''funçao que uma string onde todos os pontos de coesao textual foram substituídos por espaço; str->str'''
    a = '.'
    b = '!'
    c = '?'
    d = '...'
    e = '–'
    f = ','
    g = ':'
    h = ';'
    k = a and b and c and d and e and f and g and h
    return str.replace(frase, k, '')