def primo(n):
    for x in range (1,n+1):
        if n % x !=0 and n % n == 0 and n % 1 == 0:
            return True