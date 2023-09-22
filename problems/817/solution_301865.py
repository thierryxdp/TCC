def acima_da_media(x):
    x.append(5)
    list.sort(x)
    A = x.index(5)
    list.remove(x, 5)
    
    return x[:]