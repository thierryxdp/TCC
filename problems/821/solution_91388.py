"""
A função recebe um inteiro n e retorna o seu fatorial

Assinatura: int --> int
"""

def fatorial(n):

  """
  Para essa função foi declarada duas variáveis. A primeira é a repetição que servirá de parada para o laço de repetição while e o fatorial que será retornado no final

  Em seguida, a função entre num laço de repetição onde o fatorial é multiplicado pela repetição e depois retorna o valor do fatorial
  """

  repeticao = n - 1
  fatorial = n

  while repeticao >= 1:

    fatorial = fatorial * repeticao

    repeticao = repeticao - 1

  return fatorial