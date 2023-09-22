def primo(n):
    '''.'''
    d = 1
    
    for n%d == 0:
        if d != 1 and d != n:
            return True
        else:
            return False