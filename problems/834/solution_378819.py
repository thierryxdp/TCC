def media_matriz(m):
    '''funcao que, dada uma matriz de inteiros nao vazia,
    retorna a media aritmetica de todos seus elementos, com precisao
    de duas casas decimais.
    matriz -> float'''
    soma = 0
    elementos = 0
    media= soma/elementos
    for i in range(len(m)):
        for j in m[i]:
            soma+=j
            elementos+=1
    return round(media,2)