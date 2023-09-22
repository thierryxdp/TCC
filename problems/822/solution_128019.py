def repetidos(lista_numeros):
  """essa função recebe como entrada uma lista de numeros e retorna o numero de vezes que um elemento da lista e igual ao elemento anterior
  list->int"""
  contagem = 0
  i = 1
  while i < len(lista_numeros):
    if lista_numeros[i] == lista_numeros[i - 1]:
      contagem += 1

    i += 1

  return contagem