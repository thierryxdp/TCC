def posLetra(frase,letra,n):
    """"retorna em que posicao de uma frase ums
    ocorrencia esta, caso exista menos ocorrencias
    sera retornado o valor -1.
    str, str, int ->"""
    i = 0
    ocorrencia = 0
    while i < len(frase):
      if frase[i] == letra:
        ocorrencia += 1
      if ocorrencia == n:
        return i
      i += 1
    return -1