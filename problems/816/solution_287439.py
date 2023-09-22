def maiores(ls,n):
    for x in ls:
        y=x<=n
        list.remove(ls,y)
    return ls