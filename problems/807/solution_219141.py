def conta_frases(texto):
    interrogacao = str.count(texto,'!')
    exclamacao = str.count(texto,'?')
    ponto = str.count(texto,'.') 
    reticencias = ponto - ponto*3
    soma = interrogacao + exclamacao + ponto
    return soma