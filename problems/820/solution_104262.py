def posLetra(string,letra,ocorrencia):

  teste = 0
  pos = 0
  i = 0
  string = list(string)

  for i in range(len(string)):

    if string[i] == letra:

      teste = teste + 1

  if ocorrencia <= teste:
    
    while i != ocorrencia:

      if string[pos] == letra:

        i = i + 1
      
      pos = pos + 1
      
    return pos - 1

  else: 

    return -1