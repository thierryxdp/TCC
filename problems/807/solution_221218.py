def conta_frases(texto):
    '''jjfjdnnfkggj'''
    texto_reticencias_retiradas= str.strip(texto,'...')
    frases_pontofinal= str.count(texto_reticencias_retiradas,'.')
    frases_exclamacao= str.count(texto,'!')
    frases_interrogacao= str.count(texto,'?')
    return frases_pontofinal+frases_exclamacao+frases_interrogacao