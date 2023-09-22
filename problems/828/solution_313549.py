def primo(n):
    '''verifica se um numero N é primo ou não'''
    divisores = []
    
    for i in list(range(1, n+1)):
        if (n % i == 0):
            divisores.append(i)
    
   	if (len(divisores) == 2):
        return True
    else:
        return False