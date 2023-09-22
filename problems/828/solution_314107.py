def primo(n):
    '''A função recebe um número inteiro positivo n e retorna um valor booleano indicando
    se o número é primo (True) ou não (False).
    Parâmetro de entrada: int
    Valor de retorno: bool'''
	divisores=0
    if n==1:
        return False
    else:
    	for numero in range(1,n+1):
            if n%numero==0:
                divisores=divisores+1
            if divisores==2:
                return True
            else:
                return False