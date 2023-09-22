def acima_da_media(x):
    m = sum(x)/len(x)
    list.append(x,m)
    list.sort(x)
    return x[(list.index(x,m)+1)::]