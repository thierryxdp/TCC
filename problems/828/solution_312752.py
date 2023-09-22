def primo(nprimo):
    div = 2
    x = True
    if nprimo == 2:
        return True
    elif nprimo > 2:
        while div < nprimo:
            if nprimo % div == 0:
                x = False
            div += 1
    return x