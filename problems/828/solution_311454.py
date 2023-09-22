def primo(n):
    s=0
    for i in range(n):
        if i==0:
            s=s
        if n/i==0:
            s=s+1
    if s<3:
        return 'True'