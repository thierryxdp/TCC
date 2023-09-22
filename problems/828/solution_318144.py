def filtra(ls,p):
    r = []
    for e in ls:
        r.append(p(e))
    return r 

def primo(n):
    ls=range(1,n+1)
    if len(filtra(ls, lambda x: n%x == 0)) == 2:
    	return True
    else:
        return False