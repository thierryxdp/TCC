def primo(n):
    prime = True
    for i in range(2,n):
        if n%i == 0:
            prime = False
    return prime