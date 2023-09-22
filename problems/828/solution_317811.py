def primo(n):
    for i in range(2,n):
        if n%i==0:
            i=i+1
            return 'True'
        else:
            return 'False'