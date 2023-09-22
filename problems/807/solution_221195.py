def conta_frases(texto):
    '''jjfjdnnfkggj'''
    frases_reticencias= str.count(texto,'.'+'.')
    frases_exclamacao= str.count(texto,'!')
    frases_interrogacao= str.count(texto,'?')
    return frases_exclamacao+frases_interrogacao+frases_reticencias