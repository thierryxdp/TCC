def lingua_p(x):
    m=""
    for l in x:
        if l in "aeiouAEIOU":
            m=m+l+"p"+l
        else:
            m = m+l
    return m