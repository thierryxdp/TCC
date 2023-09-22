def carros (**kwargs):
    x = kwargs[1]
    y = kwargs[2]
    if not y:
        n = x//5
        return n
    else:
        n = x//y
        return n