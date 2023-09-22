def primo(n):
    divisores=2
    for i in range(n):
        if n%(divisores+i)==0:
            return False
    else:
        True