def primo(n):
    '''
    	essa função detecta se o número é primo ou não retornando em valor booleano
        int -> bool
    '''
    i = 1
    while i <= n:
        if n % 2 == 1:
            return True 
        else:
            return False