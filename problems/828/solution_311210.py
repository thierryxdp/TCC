def primo(n):
    '''funcao que verifica se o numero dado como entrada e primo ou nao
    int->bool'''
    i=2
    for n in range(n,n+1):
        if n%i==0:
            return 'True'
        i=i+1
    	if n%i!=0:
        	return 'False'
        i=i+1