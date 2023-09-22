def primo(n):
    numeros = range (2,n)
    y = 0
    for item in numeros:
        if n%item == 0:
            y = y + 1
    if y>0:
        return False
    else:
        return True