def primo(n):
    """Função que dada um número inteiro positivo, diz se é primo ou não"""
    """int-->bool"""
    i=2
    while i<n:
    	if n%i!=0:
            i+=1
      		else:
            	return False
  	return True