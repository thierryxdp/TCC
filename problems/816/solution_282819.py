def maiores(x:list,n:int)->list:
	list.sort(x,reverse)
    if n in x:
        returnx[list.index(x,n):]