def primo(n):
    numeros = range(1,n)
    soma = 0
    for i in numeros:
        if n % i != 0:
            soma += 1
    if soma>0:
        return False
    else:
        return True