def primo(num):
    i=1
    for i in range(num-1):
        i=i+1
        if num%i==0:
            return False
    return True