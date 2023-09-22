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