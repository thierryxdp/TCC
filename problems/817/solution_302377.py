def acima_da_media(x):
    e = list.sun(x)/len(x)
    x += [e]
    list.sort(x)
    y = x.index(e) 
    del x[:y+1]
    return x