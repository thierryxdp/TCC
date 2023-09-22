def primo(num):
    i = 0
    for elemento in range(1,num):
        if num%elemento == 0:
            i = i+1
    if i > 0:
        return false
    else:
        return true