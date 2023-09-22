def qtd_divisores(n):
    zero=0
    i=1
    while i<=n:
        if n%i==0:
            zero=zero+1
            i=i+1
        else:
            i=i+1
    return zero
def primo(N):
    if qtd_divisores(N)==2:
        return True
    else:
        return False