def primo(num):
    """Retorna se o número(num) é primo ou não em booleano.
    int->bool!"""
    numPrimo=0
    for c in range(1,num+1):
        if num%c==0:
            numPrimo+=1
    if numPrimo==2:
        return True
    else:
        return False