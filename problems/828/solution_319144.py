def primo(n):
    mult=0
    for x in range(2,n+1):
        if n%x==0:
            return False
            mult+=1
    if mult==0:
        return True