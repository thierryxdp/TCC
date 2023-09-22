def media_matriz(matriz):
    total=0
    qtd_num=0
    for l in range(len(matriz)):
        for n in range(len(l)):
            total=total+l[n]
            qtd_num+=1
    media=total/qtd_num
    return round(media,2)