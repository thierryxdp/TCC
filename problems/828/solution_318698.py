def primo(x):
    if x>=1:
        for i in range(x):
            if x%i!=0:
                return True
            else:
                return False