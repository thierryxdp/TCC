"""
A função recebe uma lista e retorna a quantidade de vezes que um elemento da lista é igual ao anterior

Assinatura: list --> int
"""

def repetidos(lista):

  """
  Para essa função foi declarada uma variável que servirá para contar o número de repetições e um if dentro de um laço for para testar todos os elementos
  """

  repeticoes = 0

  for i in range(len(lista)-1):

    if lista[i+1] == lista[i]:

      repeticoes = repeticoes + 1

  return repeticoes