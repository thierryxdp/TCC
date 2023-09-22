def lingua_p(palavra):
    r=[]
    for e in palavra:
        if e in ('a','e','i','o','u','á','é','í','ó','ú'):
            r.append(e+'p'+e)
        else:
            r.append(e)
    return str.join('',r)