def primo(numero):
    if numero == 1 or numero == 2:
        return True
    elif numero < 1:
        return False
    elif numero > 2:
        for i in range(2,numero):
            if numero % i == 0:
                return False
            else:
                return True