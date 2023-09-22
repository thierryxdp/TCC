def filtra(ls,p):
    r=[]
    for e in ls:
        if p(e):
            r.append(e)