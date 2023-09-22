def primo(n):
    p=list(range(1,n+1))
    y=5
    w=4
    for x in range (1,n+1):
        if n%p[:-2]==0:
            return 'True'
        else:
            'False'