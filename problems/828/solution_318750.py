def primo(numero):
    i = 5
    while(i * i <= numero):
        if(n % i == 0 or n % (i+2) == 0):
            return False
        i = i + 6
        return True