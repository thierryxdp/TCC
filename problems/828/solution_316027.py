def primo(num):
    for numeros in range(2,num):
        if num % numeros == 0:
            return False
        else:
            return True