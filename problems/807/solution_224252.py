def conta_frases(Texto):
    'Função que retorna o número de frases em um texto. str --> int'
    ponto= str.count(Texto,'. ')
    exclamacao= str.count(Texto,'!')
    interrogacao= str.count(Texto,'?')
    reticencias= str.count(Texto,'...')
    return ponto+exclamacao+interrogacao+reticencias