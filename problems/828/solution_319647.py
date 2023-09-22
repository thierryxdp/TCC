def filtra(ls,x):
    r = []
    
    for e in ls:
        if p(e):
            r.append(e)
    return r

def primo(x):
    r = range(1,x+1)
    if len (filtra(r,lambda y: x%y == 0)) ==2:
    	return True
    else:
        return False