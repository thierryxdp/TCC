def lingua_p(palavra):
    lp=""
    for i in range(0,len(palavra)):
        if palavra[i] in "aeioué":
            lp=lp+palavra[i]+"p"+palavra[i]
        else:
            lp=lp+palavra[i]
    return lp