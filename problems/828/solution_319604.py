def eh_div(x,n):
    if n%x == 0:
        return True
    else:
        return False

def primo(n):
    ls = range(1, n+1)
    st = list(filter(lambda x: n%x==0, ls))
    return len(st) == 2