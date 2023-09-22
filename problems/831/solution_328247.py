def lingua_p(x):
    y = str()
    for w in x:
        if w in "aoieuéáàúíó":
            y+= str(w) + 'p' + str(w)
        if w not in "aoieuéáàúíó":
            y+= str(w)
            
            
    return y