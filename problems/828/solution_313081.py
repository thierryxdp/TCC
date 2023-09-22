def primo(n):
    cont = 0
    div = []
    for i in range(n):
        if n%(i+1) == 0:
            cont += 1
            return True
        else:
            return False