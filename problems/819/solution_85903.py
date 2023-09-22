def filtra(ls,p):
    	r=[]
    for e in ls:
    	if p(e):
    		r.append(e)
        
def filtraMultiplos(ls,n):
    return filtra(ls,lambda x: x%n==0)