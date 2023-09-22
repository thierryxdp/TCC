def primo(a):
    d = false
    b = math.isqrt(a)
    for e in range(b):
        if (a//e)*e == a:
            d = true
    return d