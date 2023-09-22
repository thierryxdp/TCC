def lingua_p(palavra):
    r=[]
    for e in palavra:
        if e in ('a','e','i','o','u'):
            r.append(e+'p'+e)
        else:
            r.append(e)
    return str.join('',r)