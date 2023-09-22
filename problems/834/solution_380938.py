def media_matriz(m):
    '''funçao que dada uma matriz de inteiros não vazia, retorna a média de todos os números
    da matriz; list->int'''
    m=0
    for i in m:
        for j in i:
            m=m+j
        media=x/(len(m)*len(m[0]))
    return round(media,2)