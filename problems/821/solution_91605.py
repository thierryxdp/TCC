def fatorial(n):
  '''Função que calcula o fatorial de um dado número n
  int -> int'''

  ''' n! = (n-0)(n-1)(n-2)...(3)(2)(1) '''

  contador = 0 #Repetição do produto
  fator_mult = 2

  while contador < n:
  #Enquanto contador for menor que o número
    fator_mult *= n
    n = n-1
    contador += 1
  return fator_mult