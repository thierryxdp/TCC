def primo(n):
    """Função que dado um número inteiro positivo, verifica se este número é primo ou não"""
    """int--->bool"""
    div=0
    for i in range(2,n):
        if n%i==0:
            div+=1
	return div<0