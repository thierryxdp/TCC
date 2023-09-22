def primo(numero):
    for i in list(range(2,numero)):
        if numero%i==0:
            return bool(0)
    return bool(1)