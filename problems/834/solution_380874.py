def media_matriz(matriz):
    '''Essa função recebe uma matriz e retorna
    a média de todos os números dessa matriz, com duas casas decimais,
    list->float'''
    soma=0
    cont=0
    while cont<len(matriz):
      for n in matriz[cont]:
          soma=sum(matriz[cont])/len(matriz[cont])
      cont+=1
    return soma