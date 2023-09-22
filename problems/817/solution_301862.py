def acima_da_media(x):
    list.remove(x, 5)
    x.append(5)
    list.sort(x)
    A = x.index(5)
    
    return x[A+1:]