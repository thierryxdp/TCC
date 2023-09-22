"""
Essa função recebe um inteiro N e retorna True se ele for primo ou False caso contrário

Assinatura: int --> bool
"""

def primo(n):

  """
  Para essa função foi declarada duas variáveis: a primeiro com possíveis dividores maiores ou igual a 2 que vai sendo incrementada e a segunda é o número de divisores

  Depois disso é usado um laço de repetição para testar todos os números menores que N que são possíveis divisores

  Por fim, usando um if/else foi verificado se existia divisores de N e caso não seja o número é primo e é retornado True
  """

  possivel_divisor = 2
  divisores = 0

  while possivel_divisor < n:

    if n % possivel_divisor == 0:

      divisores = divisores + 1

    possivel_divisor = possivel_divisor + 1

  if divisores == 0:

    return True

  else:

    return False