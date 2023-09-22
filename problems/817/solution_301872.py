def acima_da_media(x):
    y = 5
    x.append(5)
    list.sort(x)
    A = x.index(y)
    list.remove(x, 5)
    
    return x[A:]