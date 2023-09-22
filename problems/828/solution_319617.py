def primo(num):
    for div in range(2,num):
        if num%div==0:
            return False
    else:
        return True