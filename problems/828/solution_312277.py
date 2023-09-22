def primo(n):
    soma = 0
    for i in range(2,n):
        if n%i == 0:
            soma = soma + 0
        else:
            soma = soma + 1
    if soma>0:
        return False
    else:
        return True