def carros(n_p,n_c=5):
    if n_p/n_c == n_p//n_c:
        return n_p/n_c
    else:
        return n_p//n_c + 1