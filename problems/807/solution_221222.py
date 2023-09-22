def conta_frases(texto):
    '''jjfjdnnfkggj'''
    frase_interrogacao= str.partition(texto,'?')
    frase_reticencias= str.partition(texto,'...')
    frase_ponto_final= str.partition(texto,".")
    frase_exclamacao= str.partition(texto,'!')
    str.count(frase_reticencias,'...')