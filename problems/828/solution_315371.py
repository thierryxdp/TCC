def primo(n):
    numeros = range (2,n)
    for item in numeros:
        if n%item == 0:
            return False
        elif n%n == 0:
            return True