def media_matriz(matriz):
    ''' Função que recebe uma matriz de inteiros não vazia, e retorna a média
    de todos os números da matriz(com exatamente duas casas decimais de precisão)
    list -> int '''

    soma =0
    elementos = 0
  
    for linha in matriz:
        for coluna in linha:
            soma = soma + coluna
            elementos = elementos + 1
      
    return round(soma/elementos,2)