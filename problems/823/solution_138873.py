def faltante(L):
  '''Função que, dada uma lista L com N − 1 inteiros numerados de 1 a N, descobre qual número inteiro deste intervalo está faltando.
  list -> int'''

  largura_lista = max(L) - 1
  list.sort(L)
  i = 0

  while i <= largura_lista:
    if L[i+1] == (int(L[i]) + 1):
      #Se o algarismo consecutivo for igual ao antecedente + 1
      i += 1
    else:
      #Se o algarismo consecutivo não for igual ao antecedente + 1, acrescente o algarismo consecutivo entre esses 2
      consecutivo = int(L[i] + 1)
      list.insert(L,L[i+1],consecutivo)
  return L