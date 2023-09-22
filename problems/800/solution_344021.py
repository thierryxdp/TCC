def mapeia(ls,f):
    r = []
    for e in ls:
        e.append(f(e))
	return r 
               
def total(ls,d):
    return sum(mapeia(ls s:d[s]))