def primo(n):
    for d in range(1,n):
        d=1
        if n==2:
            return 'True'
        elif d>1 and n%n==0 and n%d==0 and n%2!=0:
            return 'True'
        else:
            n%2==0 or 
            n%3==0 or
            n<1==0 or
            n%d!=0 or
            n%d>1
            return 'False'