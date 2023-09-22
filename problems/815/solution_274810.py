def insere(lista_numero, n):
  """dada uma lista de inteiros ordenada crescentr e um inteiro, retorna o inteiro na posição correta
list,int->list"""
  lista_numero.append(n)
  lista_numero.sort()
  return lista_numero