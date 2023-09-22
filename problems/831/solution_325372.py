def lingua_p(x):
    s=1
    l=x[:]
    for e in l:
        if e in "AEIOUaeiouáéíóú":
            x=str.replace(x,e,e+'p'+e)
            s=s+1
    return x