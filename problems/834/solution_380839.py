def media(matriz):
  '''Função que retorna a média simples dos elementos em uma matriz.
   list> int'''
  soma = 0
  tamanho = 0

  for linha in matriz:
       soma += sum(linha)
       tamanho += len(linha)

  resultado = soma / tamanho
  return round(resultado,2)