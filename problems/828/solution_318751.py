def primo(numero):
    i = 5
    while(i * i <= numero):
        if(numero % i == 0 or numero % (i+2) == 0):
            return False
        i = i + 6
        return True