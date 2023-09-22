def primo(n):
    """Função que dado um número inteiro positivo, verifica se este número é primo ou não"""
    """int--->bool"""
    div=0
    while i<n:
        if n%i!=0:
            i+=1
        else:
            return False
 	return True