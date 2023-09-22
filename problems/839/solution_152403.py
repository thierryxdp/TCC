def carros(p,v=5):
    if p%v == 0:
        return p//v
    else:
        return p//v + 1