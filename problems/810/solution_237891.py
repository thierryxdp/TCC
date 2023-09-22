def retira_pontuacao(texto):
    '''Retira toda a pontuacao de um texto e o retorna'''
    #str -> str
    texto = str.replace(texto, '.', ' ')
    texto = str.replace(texto, '?', ' ')
    texto = str.replace(texto, '!', ' ')
    texto = str.replace(texto, '...', ' ')
    texto = str.replace(texto, ',', ' ')
    texto = str.replace(texto, '-', ' ')
    texto = str.replace(texto, ':', ' ')
    texto = str.replace(texto, ';', ' ')
    return texto

def inverte(texto):
    '''Retira a pontuacao de um texto, poe todas as palavras em minusculo e retorna o texto resultante invertido'''
    #str -> str
    texto = retira_pontuacao(texto)
    texto = str.split(texto, '')[::-1]
    texto = str.join(' ', texto)
    texto = str.lower(texto)
    return texto