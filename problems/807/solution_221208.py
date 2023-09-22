def conta_frases(texto):
    '''jjfjdnnfkggj'''
    texto_sem_interrogacao= str.partition(texto,'?')
    texto_sem_exclamacao=str.partition(texto_sem_interrogacao,'!')
    return texto_sem_exclamacao