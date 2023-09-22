def primo(n):
    """ função que mostra se um numero é primo ou não;
    int-> bool"""
    divisor=[]
    for i in range (1, n + 1):
        if n%i ==0:
            list.append(divisor,i)
    if len(divisor) > 2:
        return False
    else:
        return True