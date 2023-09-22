def insere(lista_numero, n):
  """A função recebe uma lista em ordem crescente e um valor inteiro 'n' e retorna a lista
em ordem crescente com o valor 'n' adicionado
	list -> list"""
  l1 = lista_numero
  l1.insert(-1, n)
  l1.sort()
  return l1