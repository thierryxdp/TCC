def media_matriz(matriz):
    '''Função que calcula  a media de uma matriz com duas casa decimais ,int-->float'''
    soma = 0
    tamanho = 0

for linha in matriz:
    soma += sum(linha)
    tamanho += len(linha)

  return round(soma / tamanho,2)