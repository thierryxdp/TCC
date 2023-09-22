def primo(n):
    """ Essa função calcula se o número é primo. int>int"""
    primo = True
    for i in range(2, int(n+ 1)):
        if n % i == 0: 
            primo = False
            return True