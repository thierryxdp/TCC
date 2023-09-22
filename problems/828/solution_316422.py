def primo(n):
    divisores = []
    naturais = [2,3,4,5,6,7,8,9]
    for i in naturais:
        if type(n % i) == int:
            divisores.append(i)
        if len(divisores) == 0:
            return True
        else:
            return False