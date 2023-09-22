def acima_da_media(x):
    if len(x) > 1:
        e = sum(x)/len(x)
        x += [e]
        list.sort(x)
        y = x.index(e) 
        del x[:y+1]
        return x
    else:
        return []