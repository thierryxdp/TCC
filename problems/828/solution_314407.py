def primo(n):
    '''
    int ---> booloean
    funcao que retorna se um numero e primo ou não
    '''
    if n < 0:
        n = -1*n
    k = True
    if n==0 or n==1:
        k=False
    for i in range(2,n//2 + 1):
        if n%i == 0:
            k=False

    return k