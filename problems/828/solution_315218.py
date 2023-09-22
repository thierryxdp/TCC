def primo(n):
    '''Retorna se n é primo ou não
int -> bool'''
    divisores=0
    for x in list(range(1,n+1)):
        if n%x==0:
            divisores=divisores+1
    if divisores==2:
        return True
    else:
        return False