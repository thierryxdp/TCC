def lingua_p(palavra):
    lp=""
    for i in range(0,len(palavra)):
        if palavra[i] in "aeiou":
            lp=lp+palavra[i]+p+palavra[i]
    return lp