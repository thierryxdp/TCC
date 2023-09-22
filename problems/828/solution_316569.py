def primo(numero):
    divisores = 0
    for elemento in range(1,numero+1):
        if numero%elemento == 0:
            divisores += 1
    return (divisores <= 2)