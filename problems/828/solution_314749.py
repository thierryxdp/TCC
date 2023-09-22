def primo(x):
    p=[1:x]
    for h in p:
        if x%h==0:
            return False
        else:
            return True