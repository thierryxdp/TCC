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
    k = a or b or c or d or e or f or g or h
    f1 = str.replace(frase, k, '')
    return f1