def primo(n_int):
    for numero in range(2,n_int):
        if n_int%numero==0:
            return False
    return True