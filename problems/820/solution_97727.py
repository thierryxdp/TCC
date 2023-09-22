def posLetra(string,letra,n):
    """Função que retorna a posição da ocorrencia de uma letra dada no parametro
    str -> int"""
     i= 0
  ocorrencia = 0
  while i < len(string):
    if string[i] == letra:
      ocorrencia += 1
      if ocorrencia == n:
        return i
    i += 1
  if ocorrencia < n:
    return -1