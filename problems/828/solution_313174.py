def primo(n):
    '''a funçao verifica se o numero é 
       primo ou não
       int -> bool'''
    
    for i in range(1,n+1):
        if n%i==0 and i!=1 and n!=i:
            return False
        if not n%i==0 and not i!=1:
            return True