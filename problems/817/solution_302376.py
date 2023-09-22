def acima_da_media(x):
    x += [5]
    list.sort(x)
    y = x.index(5) 
    del x[:y+1]
    return x