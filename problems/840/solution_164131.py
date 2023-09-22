def bolo(a, b, c):
    farinha = a//2
    ovo = b//3
    leite = c//5
    if farinha <= ovo and farinha <= leite:
        return farinha
    elif ovo <= farinha and ovo <= leite:
        return ovo
    elif leite <= farinha and leite <= ovo:
        return leite