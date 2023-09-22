def acima_da_media(x):
    list.sort(x)
    
    if 5 in x:
        return x[list.index(x,5):]
    if 6 in x:
        return x[list.index(x,6):]
    if 7 in x:
        return x[list.index(x,7):]
    if 8 in x:
        return x[list.index(x,8):]
    if 9 in x:
        return x[list.index(x,9):]
    if 10 in x:
        return x[list.index(x,10):]
    else:
        return []