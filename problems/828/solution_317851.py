"""Recebe um numero positivo, verificando se este é ou não
primo, retornando um valor booleano.
Assinatura: int --> bool
Testes: 
primo(7) == true
primo(8) == false
"""
def primo(n):
  x = 2
  while x < n:
    if (n%x == 0):
       	return False
    x += 1
  return True