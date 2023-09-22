def primo(n):
    '''Retorna True se n é primo e False caso contrário;
    int -> bool'''
    div=0
    for i in range(1,n+1):
        if n%i==0:
            div=div+1
    if div==2:
    return True
	else:
        return False