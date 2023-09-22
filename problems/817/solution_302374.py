def acima_da_media(x):
    list.sort(x)
    y = x.index(6) 
    del x[:y+1]
    return x