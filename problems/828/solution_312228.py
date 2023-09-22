def primo(x):
    f=2
    while x%f!=0 and f<=x/2:
        f=f+1
    if x%f==0:
        return True
    else:
        return False