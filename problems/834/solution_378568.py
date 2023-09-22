def media_matriz(matriz):
    "retorna a media dos elementos de uma matriz"
    "entrada:matriz(int). saida:float."
    x=0
    y=0
    for i in matriz:
        x=x+len(i)
        y=y+sum(i)
    return round(y/x,2)