def conta_frases(texto):
    resp=texto.split('.','!','?','...')
    resp= len(resp)
    return resp