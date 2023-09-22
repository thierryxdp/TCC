def primo(n_int):
    if n_int==1:
        return False
    for numero in range(2,n_int):
        if n_int%numero==0:
            return False
    return True