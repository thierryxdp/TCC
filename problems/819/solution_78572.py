def filtraMultiplos(lnum,num):
    multi = ()
    proximo = 0
    while proximo < len(lnum):
        if lnum[proximo]%num == 0: 
        multi = multi + (lnum[proximo],)
        proximo = proximo +1
    return multi