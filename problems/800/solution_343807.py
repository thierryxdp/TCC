def total(ls,dc):
    l=list(dict.keys(dc))
    d={}
    for i in ls:
        if i in l:
            d.update({i:dc[i]})
    return d