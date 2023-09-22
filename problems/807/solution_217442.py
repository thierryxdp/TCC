def conta_frases(t):
    """Conta a quantidade de frases dentro de um texto; str->int"""
    num3pontos= t.count('...')
    numpf=t.count('.')-3*num3pontos
    return num3pontos+numpf+t.count('!')+t.count('?')