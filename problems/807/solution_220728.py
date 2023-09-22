def conta_frases(texto):
    ponto = len(texto[:].split('.',0))
    exclamacao = len(texto[:].split('!',0))
    interrogacao = len(texto[:].split('?',0))
    reticencias = len(texto[:].split('...',0))
    return ponto+exclamacao+interrogacao+reticencias