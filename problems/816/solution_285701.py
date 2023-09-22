def maiores(x:list,n):
    if n in x:
        list.sort(x)
        x[list.index(x,n):]
        if n in x[list.index(x,n):]:
            return x[list.index(x,n):][list.count(x,n):]
    else:
        list.append(x,n)
        list.sort(x)
        return x[list.index(x,n)]