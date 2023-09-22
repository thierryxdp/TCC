def media_matriz(matriz):
    """funcao que recebe uma matriz, calcula a media de todos os numeros da matriz e retorna a media com duas casas decimais.
    entrada->list(list)
    saida->float """
    l = len(matriz)
    c = len(matriz[0])
    soma = 0
  
    for i in range(l):
        for j in range(c):
            num = matriz[i][j]
            soma = soma + num
            
    return  round((soma/(l*c)),2)