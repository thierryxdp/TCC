def retira_pontuacao(texto):
    '''dado um texto, retorna o texto substituindo os caracteres de pontuação por espaço;
    str -> str'''
    texto = str.replace(texto, '—', ' ')
    texto = str.replace(texto, '-', ' ')
    texto = str.replace(texto, ',', ' ')
    texto = str.replace(texto, ':', ' ')
    texto = str.replace(texto, ';', ' ')
    texto = str.replace(texto, '...', ' ')
    texto = str.replace(texto, '!', ' ')
    texto = str.replace(texto, '?', ' ')
    texto = str.replace(texto, '.', ' ')
    
    return texto