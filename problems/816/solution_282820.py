def maiores(x:list,n:int)->list:
	list.sort(x,reverse)
    if n in x:
        return x[list.index(x,n):]