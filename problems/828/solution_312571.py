def primo(n):
    "Verifica se o número é primo ou não. int->bool"
    for i in range(2,n):
        if (n%i==0):
            return True
        else:
            return False