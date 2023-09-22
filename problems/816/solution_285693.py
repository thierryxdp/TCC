def maiores(x:list,n):
    if n in x:
        x[list.index(x,n):]
        if n in x[list.index(x,n):]:
            return list.sort(x[list.index(x,n):][list.count(x,n):])
    else:
        list.sort(x)
        return []