def primo(n):
    
    i=0
    for x in range(n):
        if n%x==0:
            i=i+1
    if i==1:
        return 'True'
    else:
        return 'False'