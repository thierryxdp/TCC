def primo(n):
    '''.'''
    d = 2
    D = 1
    a = 0
    while d < n:
        if n%d==0:
            a = a
        d = d + 1
    return bool(a)