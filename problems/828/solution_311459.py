def primo(n):
    s=0
    for i in range(n):
        if i==0:
            s=s
        elif n/i==0:
            s=s+1
    if s=<2:
        return 'True'
    else:
        return 'False'