def filtraMultiplos(lnum,n):
    div=[ ]
    i=0
    while i<len(lnum):
        if lnum[i]%n==0:
            div=div+div.append(lnum[i])
            i=i+1
        return div