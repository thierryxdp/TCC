def primo(n):
    '''função que informa se um número é primo'''
    'int---->bool'
    i=1
    par=int()
   
    while i < n :
        if n!=2 and n != par:
            par=par+n%2==0
            i+=1
           
            return True

        if  n>=2 and n==par:
            par=par+(n%2==0)
            i+=1
            
            return False