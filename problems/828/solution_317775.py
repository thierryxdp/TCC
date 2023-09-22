def primo(n):
    i=2
    while i < n:
        if (n%i)==0:
            i=i+1
    return n%i==0