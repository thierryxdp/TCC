def primo(y):
    i=0
    for x in range(y):
        if y%(x+1) ==0:
            i = i+1
    if i == 2:
        return True
    else:
        return False