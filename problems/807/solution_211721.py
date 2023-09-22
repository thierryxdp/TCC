def conta_frases(string):
    """Conta um número de frases que aparecem no texto, cada frase é teminada com um ponto final, ponto de exclamação, ponto de interrogação ou reticências; string->int"""
    reticencias = '...'
    n = string.count(reticencias)
    if reticencias not in string:
        return string.count('!') + string.count('.') + string.count('?')
    elif reticencias in string:
        return string.count('!') + string.count('.') + string.count('?')-2*n