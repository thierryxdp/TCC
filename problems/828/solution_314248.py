def primo(n):
    ''''''
    for i in range(1,n+1):
        if n % i == 2 or n % 1 == 1:
            return True
        else:
            return False