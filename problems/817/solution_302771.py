def media(m):
    return sum(m)/len(m)
def acimda_da_media(x):
    y=maiores(x, media(x))
    list.sort(y)
    return y