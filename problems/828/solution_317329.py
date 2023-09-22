def primo(n):
    '''função que informa se um número é primo'''
    'int---->bool'
    i=1
    n_primos=[]
    while i < n:
        if n >= 2 and n%2!=0:
            x=n%1==0 and n%n==0
            n_primos.append(x)
            i+=1
            print (n_primos)
            return True
        else:
            return False