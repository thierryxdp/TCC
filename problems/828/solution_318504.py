def primo(n):
    '''.'''
    d = 2
    a = 0
    while d < n:
        if n%d==0:
            d = d + 1
            a = a
    return bool(a)