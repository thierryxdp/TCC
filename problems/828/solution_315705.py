def primo(num):
    for i in range(1,num):
        if num%i+1 == 0:
            return False
        else:
            return True