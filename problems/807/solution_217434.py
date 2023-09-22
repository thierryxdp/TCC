def conta_frases(texto):
    """Conta a quantidade de frases dentro de um texto; str->int"""
    num3pontos=s.count('...')
    numpf=s.count('.')-3*num3pontos
    return num3pontos+numpf+s.count('!')+s.count('?')
#