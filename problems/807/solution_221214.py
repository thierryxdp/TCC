def conta_frases(texto):
    '''jjfjdnnfkggj'''
    texto_sem_interrogacao= str.strip(texto,'?')
    texto_sem_exclamacao=str.strip(texto_sem_interrogacao,'!')
    texto_sem_reticencias= str.strip(texto_sem_exclamacao,'...')
    texto_sem_ponto= str.strip(texto_sem_reticencias,'.')
    return texto_sem_exclamacao