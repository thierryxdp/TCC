def primo(n):
    numeros = range(1,n+1)
    soma = 0
    for i in numeros:
        if n%i == 0:
            soma = soma + 0
        else:
            soma = soma + 1
    if soma>0:
        return False
    else:
        return True