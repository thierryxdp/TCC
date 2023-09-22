def primo(x):
    if x==0 or x==1:
        return False
    for numeros in range(2,x):
        if x%numeros==0 :
            return False
    return True