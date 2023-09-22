def soma_h(N):
  '''Função que, dado um valor N, calcula e retorna o valor H da soma dos inversos dos números inteiros de 1 até N
  int -> float'''

  soma = 1
  denominador = 1

  for i in range(N-1):
    denominador += 1
    soma += (1/denominador)
  
  return round(soma,2)