# Questão 5

def fatorial(n):
  '''Função que calcula o fatorial de um dado número n
  int -> int'''
  fator_mult = 1

  while 1 <= n:
    fator_mult *= n
    n -= 1  
  return fator_mult