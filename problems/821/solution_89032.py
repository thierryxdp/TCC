def fatorial(num):
    i=0
    l=list(range(num-1,0,-1))
    l1=[]
    while i<num:
        if l[i]==l[0]:
        	l1=num*l[0]
        elif l[i]!=l[0]:
            l1=l1*l[i]
    	i=i+1
    return l1