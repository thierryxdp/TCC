def primo(n):
    '''.'''
    d = 1 
    a = 0
    while d <= n:
        if n%d == 0:
            if d > 2 and d < n:
            	a = a
            
        d = d + 1
            
    return bool(a)