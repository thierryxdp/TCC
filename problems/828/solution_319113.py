def primo(x):
    for k in range(2,x):
        if (x/2)%k > 0:
            return True
        else:
            if (x/2)%k == 0:
                return False
            else:
                if x == 2:
                    return True