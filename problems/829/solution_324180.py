"""
A função recebe um inteiro N e retorna o valor de H conforme mostrado na questão

Assinatura: int --> int
"""

def soma_h(n):

  """
  Para essa função eu usei duas variáveis que representa a soma de H e o passo de repetição para o laço while e por fim a soma é arredondada para 2 valores depois da vírgula e retornada
  """

  soma_h = 0
  passo = 1

  while passo < n + 1:

    soma_h = soma_h + (1/passo)

    passo = passo + 1

  soma_h = round(soma_h,2)

  return soma_h