def repetidos(numeros):
  '''Função que recebe uma lista de números e indica a quantidade de vezes que um elemento é igual ao elemento anterior
  list -> int'''

  i = 0
  repetido = 0

  for i in numeros:
    if numeros[i+1] == numeros[i]:
      repetido += 1
      i += 1
    else:
      i += 1
  return repetido