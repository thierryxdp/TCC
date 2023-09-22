def soma_h(n):
  """ dada a função retornar calcular e retornar o valor de h
  int -> float"""
  soma = 0
  for i in range(n):
    soma += 1/(i+1)
  return round(soma,2)