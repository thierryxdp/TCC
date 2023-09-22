"""
Essa função recebe um inteiro N e retorna o número de divisores de N

Assinatura: int --> int
"""

def qtd_divisores(n):

  """
  Para essa função basicamente foi usada o mesmo escopo da função de verificação se o número é primo ou não com algumas diferenças e retornando apenas a variável "divisores"
  """

  possivel_divisor = 1
  divisores = 0

  while possivel_divisor <= n:

    if n % possivel_divisor == 0:

      divisores = divisores + 1

    possivel_divisor = possivel_divisor + 1

  return divisores