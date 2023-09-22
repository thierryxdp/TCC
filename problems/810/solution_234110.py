def sem_pontuacao(texto):
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



# 5) Função inverte frase sem letras maiusculas e pontuação.

def inverte(texto):
    '''Dada uma frase, remove toda a sua pontuação e a inverte.
    srt -> str'''
    #removendo a pontuação
    texto_novo = sem_pontuacao(texto)
    texto_novo = str.split(texto_novo, ' ')[::-1]
    texto_novo = str.join(' ', texto_novo)
    return texto_novo