def primo(n):
    '''Verificacao de um inteiro dado como 
    argumento retorna se o numero é primo ou não.int->bool'''
    x = 0
    for i in range(2,n):
        if n%i==0:
    		x +=1
    if x>0:
    	resposta = False
    if x==0:
    	reposta = True
        
		return resposta