def primo(x):
    divisores = ()
    for divisor in range(1,x):
        if x%divisor == 0:
            divisores = divisores + (divisor,)
        return((len(divisores))<==2)