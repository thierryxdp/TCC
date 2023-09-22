def filtra(ls,p):
    r = []
    for e in ls:
        r.append(p(e))
        return r 

def primo(n):
    if len(filtra(range(1, n+1), lambda x: n%x == 0)) == 2:
    	return True
    else:
        return False