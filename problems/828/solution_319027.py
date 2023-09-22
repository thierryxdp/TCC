def primo(n):
    r=[]
    i=2
    while i<=n:
        if n%i==0:
            r.append(i)
        i=i+1
    if len(r)==1:
        return True
    else:
        return False