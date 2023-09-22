def carros(p,c=5):
    """"""
    return int((p//c) + (0 if (p//c) % 1 ==  0 else 1))