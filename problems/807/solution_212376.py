def conta_frases(texto):
    """Dado um texto, a função conta o número de frases terminadas pelos seguintes pontos:
    interrogação, exclamação, reticências e ponto final. Esses pontos não podem aparecer
    repetidos em sequência no texto;
    str --> int"""
  
    A = str.replace(texto,'...','.')
    B = str.replace(A,'!','.')
    C = str.replace(B,'?','.')
    D = str.split(C,'.')
    E = len(D)

    if C[-1] == '.':
        return E-1
    else:
        return E