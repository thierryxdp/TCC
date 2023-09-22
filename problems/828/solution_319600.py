def eh_div(x,n):
    if n%x == 0:
        return True
    else:
        return False

def primo(n):
    ls = range(1, n+1)
    ds = map(ls, eh_div)
    if len(ds)>2:
        return False
    else:
        return True
    
def ft(n):
    ls = list(range(1, n+1))
    r=1
    for e in ls:
        r = r*e
    return r