def conta_frases(texto):
    resp1=texto.split('.')
    resp2=resp1.split('!')
    resp3=resp2.split('?')
    resp4=resp3.split('...')
    resp= len(resp4)
    return resp