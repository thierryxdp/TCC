def primo(x):
    for c in range (1, x+ 1):
        divisiveis = 0
        if x%c==0:
            divisiveis += 1
        if divisiveis == 3:
            return True
        else:
            return False