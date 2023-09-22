def lingua_p(x):
    m=""
    for l in x:
        if l in "aeiouAEIOUáéíóú":
            m=m+l+"p"
        else:
            m = m+l
    return m