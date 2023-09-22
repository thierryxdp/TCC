def primo(num):
    for i in range(num):
        i+=2
        if num%i==0:
            return False
    return True