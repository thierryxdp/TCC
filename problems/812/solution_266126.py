def retira_pontuacao(texto):
    '''Retorna a frase com suas pontuações substituidas por espaço
    	str -> str'''
    texto = str.replace(texto, '.', ' ')
    texto = str.replace(texto, ',', ' ')
    texto = str.replace(texto, ';', ' ')
    texto = str.replace(texto, ':', ' ')
    texto = str.replace(texto, '!', ' ')
    texto = str.replace(texto, '-', ' ')
    texto = str.replace(texto, '...', ' ')
    texto = str.replace(texto, '?', ' ')
    return texto