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

def inverte(frase):
    texto = retira_pontuacao(frase)
    texto = str.lower(texto)
    texto = str.split(texto)
    list.reverse(texto)
    return str.join (' ',texto)