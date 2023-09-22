def fatorial(num):
    i=0
    l=list(range(num-1,0,-1))
    l1=[]
    while i<num:
        if f[i]==f[0]:
        	l1=num*l[0]
        if f[i]!=f[0]:
            l1=l1*f[i]
    	i=i+1
    return l1