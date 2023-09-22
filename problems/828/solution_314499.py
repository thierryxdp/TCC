def primo(num):
    i=2
    for i in range(num-1):
        if not num%i!=0:
            return False
    return True