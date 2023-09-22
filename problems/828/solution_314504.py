def primo(num):
    for i in range(num-1):
        if i>1 and num%i==0:
            return False
    return True