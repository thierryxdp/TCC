def primo(n):
    '''.'''
    d = 1
    
    while d <= n:
        if d == 1 or d == n and n%d == 0:
            return True
        else:
            return False