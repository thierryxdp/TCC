def conta_frases(texto):
    interrogacao = str.count(texto,'!')
    exclamacao = str.count(texto,'?')
    ponto = str.count(texto,'.')
    soma = interrogacao + exclamacao + ponto
    return soma