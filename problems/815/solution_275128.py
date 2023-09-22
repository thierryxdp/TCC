"""
Essa função recebe uma lista de números ordenados crescentemente e um número e retorna uma nova lista ordenada com esse núemero no lugar correto

Assinatura: list, int --> list
"""

def insere(lista_numero,n):

  """
  Nessa função simples foi usada a função "sorted" que ordena uma lista e antes disso foi adicionado o elemento n na lista para em seguida ser ordenada
  """

  nova_lista = lista_numero + [n]

  nova_lista_ordenada = sorted(nova_lista)

  return nova_lista_ordenada