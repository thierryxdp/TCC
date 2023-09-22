def primo(n):
    divisores=0
    for x in range(2,n):
        if n%x==0:
            divisores+=1
    if divisores>0:
        return False
    else:
        return True