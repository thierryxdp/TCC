def primo(n):
    '''Dado um numero inteiro positivo(n), confere se o numero é primo.int->boolean''' 
    i=0
    j=1
    k=0
    if n<=0:
        return 0       
    while i<n:
        if n%j==0:
            k=k+1
            j=j+1
        else:
            j=j+1
        i=i+1
    if k==2:
        return True
    else:
        return False