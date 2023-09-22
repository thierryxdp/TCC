def media_matriz(matriz):
    '''
    Função que dada uma matriz de inteiros não vazia,
    retorna a média dos numeros d matriz, com precisão de
    duas casas decimais
    '''
    soma = 0
    for l in matriz:
        for n in linha:
            soma = soma+n
        total = soma/(len(matriz)*len(matriz[0]))
    return round(total,2)