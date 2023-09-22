def media_matriz(matriz):
    ''' Função que recebe uma matriz de inteiros não vazia, e retorna a média
    de todos os números da matriz(com exatamente duas casas decimais de precisão)
    list -> int '''

    soma =[]
    elementos = 0
  
    for linha in matriz:
        for coluna in linha:
            soma = soma + [coluna]
            elementos = elementos + 1
      
    return round(sum(soma)/elementos,2)