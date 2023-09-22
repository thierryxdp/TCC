def media_matriz(x):
    '''Função que dada uma matriz, retorna a
    media dos numeros da matriz. matriz->bool
    matriz-> int'''
    soma = 0  
    for linha in x:
        soma += sum(linha)
    return round(soma/(len(x)*len(x[0])),2)