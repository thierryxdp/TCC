def primo(num):
    mult = 0
    for i in list(range(2, num)):
        if num % i == 0: 
             mult = mult + 1
    if mult == 0:
        return True
    else:
        return False