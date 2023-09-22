def media_matriz(x):
    '''Dada uma matriz x de números inteiros, calcula a média.
    list -> int'''
    b=0
    y=0
    for i in range(len(x)):
        for j in range(len(x[i])):
            b+=1
            y+=x[i][j]
    media=y/b
    return round(media,2)