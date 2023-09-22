def filtra(ls,p):
    r = []
    for e in ls:
        r.append(f(e))
        return r 

def primo(n):
    return len(filtra(range(1, n+1), lambda x: x%n == 0)) == 2