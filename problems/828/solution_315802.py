def primo(n):
    for d in range(1,n+1):
        if n % d != 0 and n % 1 == n and n % n == 1:
            return True 
        else: 
            return False