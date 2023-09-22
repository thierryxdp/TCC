def primo(num):
    div = 0
    for i in range(2,num+1):
        if (num%i==0):
            div = div + 1
    if (div!=1):
        return False
    else:
        return True