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
    f1 = str.replace(frase, a, '')
    f2 = str.replace(frase, b, '')
    f3 = str.replace(frase, c, '')
    f4 = str.replace(frase, d, '')
    f5 = str.replace(frase, e, '')
    f6 = str.replace(frase, f, '')
    f7 = str.replace(frase, g, '')
    f8 = str.replace(frase, h, '')