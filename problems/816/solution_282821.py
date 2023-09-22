def maiores(x:list,n:int)->list:
	list.sort(x,reverse=True)
    if n in x:
        return x[list.index(x,n):]