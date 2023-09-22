def retira_pontuacao(texto):
    '''Dada uma frase, retorna a mesma com espaço no lugar de pontuação.
    str -> str'''
    texto_modificado = ''
    texto_modificado = str.replace(texto, '...', '')
    texto_modificado = str.replace(texto_modificado, '.', '')
    texto_modificado = str.replace(texto_modificado, '!', '')
    texto_modificado = str.replace(texto_modificado, '?', '')
    texto_modificado = str.replace(texto_modificado, ',', '')
    texto_modificado = str.replace(texto_modificado, '-', ' ')
    texto_modificado = str.replace(texto_modificado, ':', '')
    texto_modificado = str.replace(texto_modificado, ';', '')
    return texto_modificado