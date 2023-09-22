def conta_frases(texto):
    ponto=str.count(texto,'.',)
    exclamacao=str.count(texto,'!')
    interrogacao=str.count(texto,'?')
    reticencias=str.count(texto,'...')
    if '...'in texto:
        return pontodeexclamacao+exclamacao+interrogacao-2*reticencias
    else:
        return ponto+exclamacao+interrogacao