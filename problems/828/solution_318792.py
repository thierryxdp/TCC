def primo(num):
    for x in range(2,num-1):
        if num%x==0:
            return True
    else:
        return False