def filtraMultiplos(listn,n):
    v=0
    div=[]
    t=len(listn)
    while t!=v:
        if listn[v] % n == 0:
            div.append(listn[v])
        v=v+1
    return div