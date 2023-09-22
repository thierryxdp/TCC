"""
Essa função filtra os múltiplos de um certo número n. Esse número n é um inteiro e é passado como argumento para a função que também recebe uma lista de números e retorna outra lista contendo apenas os múltplos de n

Assinatura: list, int --> list
"""

def filtraMultiplos(lista,n):

  """
  Para essa função primeiro foi declarada uma nova lista para armazenar os múltiplos em seguida foi usando for e if para testar todos os valores da lista passada e por fim retorna a lista dos múltiplos
  """

  multiplos = []

  for i in range(len(lista)):

    if lista[i] % n == 0:

      multiplos = multiplos + [lista[i]]

  return multiplos