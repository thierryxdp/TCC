def conta_frases(texto):
    "essa funcao calcula e retorna o numero de frases que aparecem no texto onde possuem um simbolo ao final de cada uma;str ->int"
    ponto=str.count(texto,'.')
    reticencias=str.count(texto,'...')
    interrogacao=str.count(texto,'?')
    exclamacao=str.count(texto,'!')
    
    return ponto -3*reticencias+reticencias+interrogacao+exclamacao