def primo(num):
    i=0
    for numeros in list(range(2,num)):
        if num % numeros == 0:
            i=i+1
        elif i>2:
            return False
        else:
            return True