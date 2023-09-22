def maiores(ls,n):
    for x in ls:
        y=x<=n
        if y in ls:
            list.remove(ls,y)
            return ls
        else:
            return []