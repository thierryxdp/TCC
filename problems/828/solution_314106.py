def primo(n):
    '''A função recebe um número inteiro positivo n e retorna um valor booleano indicando
    se o número é primo (True) ou não (False).
    Parâmetro de entrada: int
    Valor de retorno: bool'''
    '''divisores=0
    #Número 1 não é número primo
    if n==1:
        return False
    #Número primo é aquele que só é dividido por 1 e por ele mesmo, ou seja,
    #que só tem 2 divisores
    else:
    	for numero in range(1,n+1):
            if n%numero==0:
                divisores=divisores+1
            if divisores==2:
                return True
            else:
                return False