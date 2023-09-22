def faltante(L):
    '''Recebe uma lista,L, e retorna o numero 
    que falta para completar a lista de 1 até N
    list->int'''
    li_compl=list(range(1,max(L)+1))
    i=0
    lis=[]
    if L==li_compl:
        return (max(L)+1)
    else:
    	while i<len(L):
        	if L[i]!= li_compl[i]:
            	lis=lis+[i+1]
        	i=i+1
        return lis[0]