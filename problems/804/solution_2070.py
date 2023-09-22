def filtra_pares(x):
    '''retorna uma nova tupla contendo apenas os elementos pares. tupla->tupla.'''
	a,b,c,d=x
	t=a%2
	u=b%2
	p=c%2
	l=d%2
    if t==0 and u==0 and p==0 and l==0:
        return (a,b,c,d)
    if t!=0 and u==0 and p==0 and l==0:
        return (b,c,d)
    if t==0 and u!=0 and p==0 and l==0:
        return (a,c,d)
    if t==0 and u==0 and p!=0 and l==0:
        return (a,b,d)
    if t==0 and u==0 and p==0 and l!=0:
        return (a,b,c)
    if t!=0 and u!=0 and p==0 and l==0:
        return (c,d)
    if t!=0 and u==0 and p!=0 and l==0:
        return (b,d)
    if t!=0 and u==0 and p==0 and l!=0:
        return (b,c)
    if t==0 and u!=0 and p!=0 and l==0:
        return (a,d)
    if t==0 and u!=0 and p==0 and l!=0:
        return (a,c)
    if t==0 and u==0 and p!=0 and l!=0:
        return (a,b)
    if t!=0 and u!=0 and p!=0 and l==0:
        return (d,)
    if t!=0 and u!=0 and p==0 and l!=0:
        return (c,)
    if t!=0 and u==0 and p!=0 and l!=0:
        return (b,)
    if t==0 and u!=0 and p!=0 and l!=0:
        return (a,)