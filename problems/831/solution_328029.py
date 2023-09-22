def lingua_p(palavra):
    w=str.lower(palavra)
    x=list(w)
    pp=""
    for k in x:
        pp=pp+k
        if k in ("aeiou"):
            pp=pp+"p"+k
    return pp