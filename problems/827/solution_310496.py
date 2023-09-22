def filtra (rs, predicado):
    ret = []
    for r in rs:
        if predicado (r):
            list.append(ret,r)
def qtd_divisores (n):
    ls= range(1,n+1)
    ds=filtra (ls, lambda x: n%x ==0)
    return len(ls)