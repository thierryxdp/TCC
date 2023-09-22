def primo(n):
    prime = True
    for i in range(3,n,2):
        if n%2 == 0 or n%i == 0:
            prime = False
    return prime