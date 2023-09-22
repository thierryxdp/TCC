def primo(x):
    if x%2 ==0:
        return False
    for _ in range(3,x,2):
        if x%_==0:
            return False
    return True