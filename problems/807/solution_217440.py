def conta_frases(texto):
    """Conta a quantidade de frases dentro de um texto; str->int"""
    num3pontos= str.count('...')
    numpf=str.count('.')-3*num3pontos
    return num3pontos+numpf+ str.count('!')+str.count('?')