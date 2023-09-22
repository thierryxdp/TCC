def melhor_volta(a):
    d=a[0][0]
    c=0
    l=0
    for i in range(len(a)):
		for j in range(len(a[i])):
			if(d>a[i][j]):
                d=a[i][j]
                c=i
                l=j
	return (c+1,d,l+1)