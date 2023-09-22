def primo(x):
    for divisor in range(1,x+1):
        if x%divisor == 0:
            divisores = divisores + (divisor,)
        return((len(divisores))==2)