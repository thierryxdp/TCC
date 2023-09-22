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
def inverte(frase):
    '''Retorna a frase dada como parâmetro invertida e sem pontuação
    	str -> str'''
    frase = str.split(retira_pontuacao(str.lower(frase)), '')
    return str.join(' ', frase[:-1])