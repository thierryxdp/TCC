def primo(x):
    """
    Função que diz se um número "x" é primo ou não.
    int -> Boolean
    """
    
    for i in range(2,int(x**1/2)+1):
        if x%i==0:
            return False
    return True


    #primo(411) -> False
    #primo(7) -> True