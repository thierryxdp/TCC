def media_matriz(matriz):
    '''função que dado uma matriz de inteiros (nao vazia),
    retorna a media de todos os elementos dessa matriz com
    exatamente duas casas decimais de precisão.
    list(list) -> float'''
    j = 0
    soma = 0 
    elementos = 0
    i = 0
    while i < len(matriz):
        c = sum(matriz[j])
        soma = soma + c
        d = len (matriz[j])
        j = j + 1
        elementos = elementos + d
        i = i + 1
    return round(soma/elementos,2)