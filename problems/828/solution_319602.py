def eh_div(x,n):
    if n%x == 0:
        return True
    else:
        return False

def primo(n):
    ls = range(1, n+1)
    ds = map(ls, lambda x: n%x==0)
    if len(ds)>2:
        return False
    else:
        return True