def primo(x):
    if x>=1:
        for i in range(2,x):
            if x%i!=0:
                return True
            else:
                return False