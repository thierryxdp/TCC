def posLetra(string,letra,n):
    """str -> int"""
    def posLetra(string,letra,n):
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