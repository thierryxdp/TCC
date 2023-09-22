def qtd_divisores(n):
    """Função que calcula a quantidade de divisores naturais
    de um número n.
    int --> int """
    div=0
    if(n>0):
    	for i in range(1,10000):
        	if(n%i==0):
            	div+=1
    	return div
    if(n<=0):
        return 0
    
def primo(n):
	return qtd_divisores(n)==2