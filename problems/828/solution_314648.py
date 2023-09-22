def primo(numero): 
    for n in range(2,numero+1): 
        if numero//n==1: 
            return (True)
        else:
            return (False)