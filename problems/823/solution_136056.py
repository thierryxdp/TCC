def faltante(L):
    li_compl=list(range(1,max(L)+1))
    i=0
    lis=[]
    if L=li_compl:
        return (max(L)+1)
    else:
    	while i<len(L):
        	if L[i]!= li_compl[i]:
            	lis=lis+li_compl[i]
        	i=i+1
        return lis[0]