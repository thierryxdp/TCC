""" Recebe duas listas de tamanho 3 e retorna uma lista de tamanho 6

Assinatura: list[int,int,int], list[int,int,int] --> list[int,int,int,int,int,int] """
def intercala(lista1,lista2):

  """
  A função vai intercalando as duas listas para criar uma nova usando o indíce 0, 1 e 2 das listas originais e depois retorna a terceira lista
  """

  lista3 = [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]

  return lista3