def conta_frases(texto):
    '''jjfjdnnfkggj'''
    frase_interrogacao= str.partition(texto,'?')
    frase_reticencias= str.partition(texto,'...')
    frase_ponto_final= str.partition(texto,".")
    return frase_ponto_final