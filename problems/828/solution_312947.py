def primo(n): 
    '''função que, dado um número 'n', verifique se ele é primo ou não.
    int -> bool'''
    for x in range(2,n):
        if n%x==0:
            return True
    return False