def soma_h(n):
  '''dada a variante, ela calcula e retona o valor da soma de elementos da função. int->float.'''
  soma = 0
  for i in range(n):
    soma += 1/(i+1)
  return soma