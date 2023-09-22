def media_matriz(matriz):
    '''função que retorna a média (com aproximação de 2 casas) 
    de uma matriz não vazia
    com números inteiros
    valor de entrada: lista
    valor de saída: int '''
    
   soma = 0
   tamanho = 0

  for linha in matriz:
    soma += sum(linha)
    tamanho += len(linha)

  return round(soma / tamanho,2)