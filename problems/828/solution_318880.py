def primo(n):
    i = 1
    s = 1
    while i < n:
        s= (s * i)
        i= i + 1
    return s+1%n==0