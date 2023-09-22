def primo(n):
    """k"""
    i=1
    lis=[]
    while i<=n:
        if n%i ==0:
            lis=lis+[i]
            i=i+1
        else:
            i=i+1
    if len(lis)==2:
        return True
    else:
        return False