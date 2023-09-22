def primo(n):
    p = True
    if num != 1 &  num != 2:
        for i in range(2,num):
           if (num % i) == 0:
               p = False
    return p