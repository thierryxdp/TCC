def conta_frases(texto):
    '''Dado um texto, retorna quantas frases há nele, dividindo por pontos finais, reticencias, pontos de exclamação de de interrogação.
    str -> int'''
      return (str.count(texto, '.') //2) + str.count(texto, '!') + str.count(texto, '?') + (str.count(texto, '...') // 4)