def primo(n):
    '''define se um numero é primo;
    int->bool'''
	divisores=[]
    for numero in range(1,n+1):
        if n%numero==0:
            list.append(divisores,numero)
	if len(divisores)==2:
        return True
    else:
        return False