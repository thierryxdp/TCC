def conta_frases(texto):
    '''Dado um texto, retorna o número de frases que existem no texto,
    str-> int''' 
    A=str.count(texto,'?')
    B=str.count(texto,'!')
    C=str.count(texto,'.')
    D=str.count(texto,'...')
    return A+B+(C-3*D)+D