def primo(x):
    n = int(input("x"))
    ds = 0
    for d in range(1, n):
        if n%d == 0:
            ds = ds+1
            if ds>1:
                break
    if ds>1:
        return False
    else:
        return True