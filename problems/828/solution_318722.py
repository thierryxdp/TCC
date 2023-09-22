def primo(x):
    divisores=()    
    for divisor in range(1,x+1):
        if x%divisor == 0:
            divisores = divisores + (divisor,)
    return(int(len(divisor))==2)