def conta_frases(texto):
    '''jjfjdnnfkggj'''
    frases_pontofinal = str.count(texto,'.')
    frases_exclamacao= str.count(texto,'!')
    frases_interrogacao= str.count(texto,'?')
    frases_reticencias= str.count(texto,'.''.''.')
    return frases_pontofinal+frases_exclamacao+frases_interrogacao+frases_reticencias