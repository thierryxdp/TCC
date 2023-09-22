def uppCons(f):
    r=""
    d=[b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z]
    for e in f:
        if e in d:
            r=r+str.upper(e)
        else:
            r=r+e
	return r