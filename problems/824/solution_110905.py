def uppCons (frase):
    x=list(frase)
    k=0
    j=[]
    while k<len(x):
        if x[k]not in (a,e,i,o,u,A,E,I,O,U):
            j=j+str.upper(x[k])
        else:
            j=j+x[k]
        k=k+1
	return j