def primo(n):
    p = True
    if n != 1 &  n != 2:
        for i in range(2,n):
           if (n % i) == 0:
               p = False
    return p