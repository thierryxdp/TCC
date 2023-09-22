def lingua_p(x):
    m=""
    for l in x:
        if l in "aeiouAEIOU":
            m=l+"p"+m
        else:
            m = m+l
    return m