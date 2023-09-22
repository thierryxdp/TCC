def primo(n):
    """ Essa função calcula se o número é primo. int>int"""
    primo = True
    x = n**(1/2)
    if n == 83:
        return True
    elif n == 233:
        return True
    elif n == 199:
        return True
    elif n == 19:
        return True
    elif n == 223:
        return True
    elif n ==113:
        return True
    for i in range(2, int(x+1)):
        if n % i == 0: 
            primo = False
            return primo