def primo(n):
    '''funcao retorna se n é primo ou não'''
    lista=[]
    for i in range(1,n+1):
        if n%i==0:
            lista.append(i)
    if n>0 and len(lista)==2:
    	return True
    else:
        return False