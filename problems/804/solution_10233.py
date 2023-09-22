def filtra_pares(a,b,c,d):
    '''retorna uma tupla com os numeros pares de entrada
    int,int,int-->tupla'''
    a=a%2
    b=b%2
    c=c%2
    d=d%2
	if a==0 and b==0 and c==0 and d==0:
    	return(a,b,c,d)
    if a==0 and b==0 and c==0 and d!=0:
        return(a,b,c)
    if a==0 and b==0 and c!=0 and d==0:  
        return(a,b,d)
    if a==0 and b!=0 and c==0 and d==0:
        return(a,c,d)
    if a!=0 and b==0 and c==0 and d==0:
    	return(b,c,d)