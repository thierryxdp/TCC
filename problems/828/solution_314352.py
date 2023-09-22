def primo(n:int)-> bool:
    '''Função que dado um número inteiro positivo, verifique se este número  ́e primo
ou não.'''
    if n>=2:
    	for i in range(2,n):
        	if not(n%i):
          		return False
    else:
    	return False
    return True