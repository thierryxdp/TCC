def primo(x):
    i=2
    while i<(x-1):
        if x%i==0:
            return False
        else:
            i=i+1
            if i==x-1:
                return True