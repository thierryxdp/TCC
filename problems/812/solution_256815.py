def retira_pontuacao(texto):
    '''função que, dado um texto, retorna este texto
       sem pontuação. str -> str'''
    texto = str.replace(texto, '...', '@')
    texto = str.replace(texto, '.', ' ')
    texto = str.replace(texto, '@', ' ')
    texto = str.replace(texto, '!', ' ')
    texto = str.replace(texto, '?', ' ')
    texto = str.replace(texto, ',' ' ')
    texto = str.replace(texto, ';', ' ')
    texto = str.replace(texto, ':', ' ')
    texto = str.replace(texto, '-', ' ')
    return texto