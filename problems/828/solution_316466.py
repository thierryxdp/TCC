def primo(n):
    divisores = []
    if n < 2:
        return False
    else:
        for x in range(n):
            if n%(x+1) == 0:
                list.append(divisores, x)
    return len(divisores)<3