def primo(n):
    divisores = []
    naturais = [2,3,5,7]
    for i in naturais:
        if type(n%i) == int:
            divisores.append(i)
        if len(divisores) == 0:
            return True
        else:
            return False