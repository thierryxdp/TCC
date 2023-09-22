def primo(n):
    '''função que informa se um número é primo'''
    'int---->bool'
    i=1
   
    n_primo=int()
    while i < n :
        if n >=i :
            i+=1
            n_primo=n_primo+(n%i==0)==True
            n_primo=n_primo+(n%n==0)==True
    i+=1       
    return (n_primo)
    i+=1