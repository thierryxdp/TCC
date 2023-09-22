def inverte(frase):
    '''funçao que retorna a string de entrada com a ordem das palavras, com letras minúsculas e sem pontuação; str->str'''
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
    k9 = str.lower(k8)
    k10 = str.split(k9)
    k11 = list.reverse(k10)
    return k11