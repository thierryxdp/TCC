def primo(n):
    i = 1
    s = 1
    while i < n:
        s= (s * i)%n
        i= i + 1
    return not s%n==0