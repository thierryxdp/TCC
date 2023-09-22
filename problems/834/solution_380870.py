def media_matriz(matriz):
    '''Essa função recebe uma matriz e retorna
    a média de todos os números dessa matriz, com duas casas decimais,
    list->float'''
    cont=0
    soma=0
    for n in matriz[cont]:
       soma=sum(matriz[cont])/len(matriz[cont])
    cont+=1
    return soma