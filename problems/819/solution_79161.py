def filtraMultiplos(l,n):
    x=0
    r=[]
    while x>len(l):
        if l[x]%n==0:
            r.append(l[x])
		x+=1
   	return r