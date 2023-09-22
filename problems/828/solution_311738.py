def primo(n):
    mult=0
    for i in range(2,n):
        if n%i==0:
            return('multiplo',i)
        mult=mult+1
        if mult==0:
            return True
        else:
            return False