def retira_pontuacao(frase):
    '''funçao que uma string onde todos os pontos de coesao textual foram substituídos por espaço; str->str'''
    a = '.'
    b = '!'
    c = '?'
    d = '...'
    e = '-'
    f = ','
    g = ':'
    h = ';'
    i = ' '
    k1 = str.replace(frase, a, i)
    k2 = str.replace(k1, b, i)
    k3 = str.replace(k2, c, i)
    k4 = str.replace(k3, d, i)
    k5 = str.replace(k4, e, i)
    k6 = str.replace(k5, f, i)
    k7 = str.replace(k6, g, i)
    k8 = str.replace(k7, h, i)
    frase = k8
    return frase