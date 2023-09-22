def retira_pontuacao (x):
    '''Retorna a frase fornecida substituindo as pontuações por espaços vazios.
    str -> str'''
    x1 = str.replace (x, '.', ' ')
    x2 = str.replace (x1, '...', ' ')
    x3 = str.replace (x2, '!', ' ')
    x4 = str.replace (x3, '?', ' ')
    x5 = str.replace (x4, ',', ' ')
    x6 = str.replace (x5, '-', ' ')
    x7 = str.replace (x6, ':', ' ')
    x8 = str.replace (x7, ';', ' ')
    return x8

def inverte_inversa (a):
    '''Retorna a frase sem pontuação e com as palavras na ordem inversa.
    str -> str'''
    l = str.split (retira_pontuacao(a))
    return str.lower(str.join(' ', l[::-1]))