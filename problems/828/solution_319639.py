def primo(x):
    divisores = [2,3,4,5,6,7,8,9]
    for i in divisores:
        if x % i == 0:
            return False
        else:
            return True