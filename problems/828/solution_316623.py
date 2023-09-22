def primo(n):
    '''função que retorna se um numero é ou nao primo
    int--->bool'''
    if n%2== 0:
        return False
    for i in range(3,n,2):
        if n%i==0:
            return False    
    return True