def inverte(texto):
    '''Dada uma frase, remove toda a sua pontuação e a inverte.
    srt -> str'''
    #removendo a pontuação
    texto_novo = sem_pontuacao(texto)
    texto_novo = str.split(texto_novo, ' ')
    texto_novo = str.join(' ', texto_novo)[::-1]
    return texto_novo