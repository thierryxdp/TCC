def conta_frases(texto):
    '''jjfjdnnfkggj'''
    texto_sem_interrogacao= str.partition(texto,'?')
    texto_sem_exclamacao=str.partition(texto_sem_interrogacao,'!')
    texto_sem_reticencias= str.strip(texto_sem_exclamacao,'...')
    return texto_sem_reticencias