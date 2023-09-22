def retira_pontuacao(texto):
    '''Retorna a frase com suas pontuações substituidas por espaço
    	str -> str'''
    str.replace(texto, '.', ' ')
    str.replace(texto, ',', ' ')
    str.replace(texto, ';', ' ')
    str.replace(texto, ':', ' ')
    str.replace(texto, '!', ' ')
    str.replace(texto, '-', ' ')
    str.replace(texto, '...', ' ')
    str.replace(texto, '?', ' ')
    return text