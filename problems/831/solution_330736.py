def lingua_p(palavra):
    s=()
    i=0
    while i<len(palavra):
        if palavra[i] in 'bcdfghjklmnpqrtvwxyz':
            s+=palavra[i]
        i+=1
    return s