"""Recebe um numero positivo, verificando se este é ou não
primo, retornando um valor booleano.
Assinatura:
Testes:
"""



def primo(n):
  i = 2
  while i < n:
    if (n%i == 0):
       	return False
    i += 1
  return True