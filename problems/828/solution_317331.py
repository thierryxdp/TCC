def primo(n):
    '''função que informa se um número é primo'''
    'int---->bool'
    i=1
    
    while i < n:
        if n >= 2 and n%2!=0:
            x=n%1==0 and n%n==0
            
            i+=1
            
            return True
        else:
            return False