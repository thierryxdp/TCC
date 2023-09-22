def primo(a):
    d = True
    b = math.isqrt(a)
    for e in range(b):
        if (a//e)*e == a:
            d = False
    return d