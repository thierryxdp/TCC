def primo(x):
    for divisor in range(1,x+1):
        if x%divisor == 0:
        return((len(divisor))==2)