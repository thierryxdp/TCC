def filtra(rs, predicado):
    ret = []
    for r in rs:
        if predicado(r):
            list.append(ret, r)
    return  ret 

def qtd_divisores(n):
    ls=[range]
    ds=filtra(ls, lambda x: n%x==0)
    return len(ds)