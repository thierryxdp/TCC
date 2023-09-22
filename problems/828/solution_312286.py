def primo(n):
    numeros = range(2,n)
    for i in numeros:
        if n % i == 0:
            return False
    return True