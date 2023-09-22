def posLetra(string,letra,ocorrencia):

  pos = 0
  i = 0
  string = list(string)

  while i != ocorrencia:

    if string[pos] == letra:

      i = i + 1
      
    pos = pos + 1
      
  return pos - 1