def primo(x):
    """
    Função que diz se um número "x" é primo ou não.
    int -> Boolean
    """


    if x > 1:
        for i in range(2, x):
            if (x%i) == 0:
                return False
            else:
                return True
        
    else:
        return False


    #primo(411) -> False
    #primo(7) -> True