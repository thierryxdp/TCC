def primo(n):
    
    i=0
    for x in range(n):
        if n%(x+1)==0:
            i=i+1
    if i==1:
        return 1
    else:
        return 0