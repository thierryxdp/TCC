def lingua_p(x):
    s=1
    for e in x:
        if e in "AEIOUaeiou":
            str.replace(x,e,'p'+e)
            s=s+1
    return x