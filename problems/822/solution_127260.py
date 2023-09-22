def repetidos(x):
	i=0
	k=0
	while i<((len(x))-1):
        if x[i]==x[1+i]:
            k=k+1
        i=i+1
        return k