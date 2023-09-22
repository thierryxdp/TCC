def posLetra(string,letra,n):
  i= 0
  ocorrencia = 0
  while i < len(string):
    if n > len(string)-1:
      return -1
    
    else:
      if string[i] == letra:
        ocorrencia += 1
        if ocorrencia == n:
          return i
    i += 1