def primo(n):
    '''Essa função diz se o numero 'n' é primo ou não. int -> int'''
    a=0
    i=1
    while i <= n:
        if n%i == 0:
            a+=1
        i+=1
    if a<= 2:
        return True
    else:
        return False