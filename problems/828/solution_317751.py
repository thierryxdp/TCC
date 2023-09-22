def primo(num):
    total = 0
    for div in range(num+1):
        if div != 0 and div != 1:
            if num%div == 0:
                total+=1
    if total == 1:
        return True
    else:
        return False