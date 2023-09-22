def repetidos(numeros):
  '''Função que recebe uma lista de números e indica a quantidade de vezes que um elemento é igual ao elemento anterior
  list -> int'''

  i = 0
  repetido = 0

  while i < len(numeros):
    if numeros[i] == numeros[i-1]:
      repetido += 1
      i += 1
    else:
      i += 1
  return repetido