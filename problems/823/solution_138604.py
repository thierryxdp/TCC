"""
Essa função recebe uma lista de tamanho N-1 que varia entre 1 até N mas com um valor entre esse intervalo faltando e retorna qual é esse valor faltante

Assinatura: list --> int
"""

def faltante(lista):

  """
  Para essa função eu declarei uma variável chamada peca que representa o valor da peça inicial e depois usei o laço de repetição for junto de if para testar se o valor do elemento no indíce i da lista corresponde ao valor da peça já que a lista tá ordenada. Caso os valores forem diferentes é retornado o valor da peça faltante
  """

  peca = 1
  
  for i in range(len(lista)):

    if lista[i] != peca:

      return peca

    peca = peca + 1