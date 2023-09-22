def maiores(ls,n):
    for x in ls:
        if x>n:
            ls==ls[n:]
            list.sort(ls)
            return ls