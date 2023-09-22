def conta_frases(texto):
    '''Função que retorna o número de frases dado um texto
    str -> int'''
    n_pontos = str.count(texto,'.')
    n_exclamacoes = str.count(texto,'!')
    n_interrogacao = str.count(texto,'?')
    n_reticencias = str.count(texto,'...')-3*str.count(texto,'...')
    n_total = n_pontos+n_exclamacoes+n_interrogacao+n_reticencias
    return n_total