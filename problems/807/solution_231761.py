def conta_frases(frase):
    '''Dado um texto, a função conta o número de frases no texto, considerando que as frases terminam com ponto final, interrogação, exclamação, ou reticências.
    str -> int'''

    soma = 0

    if '.' in frase:
      soma += 1
    if '!' in frase:
      soma += 1
    if '?' in frase:
      soma += 1
    if '...' in frase:
      soma += 1

    return soma