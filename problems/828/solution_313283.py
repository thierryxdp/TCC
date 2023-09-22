def primo(n):
    """ Essa função calcula se o número é primo. int>int"""
    primo = True
    x = n**(1/2)
    for i in range(2, int(x+1)):
        if n % i == 0: 
            primo = False
            return primo