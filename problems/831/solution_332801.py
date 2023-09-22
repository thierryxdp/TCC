def lingua_p(x):
    vogal=('a','á','e','é','i','o','u','ú')
    l=[]
    for i in x:
        if i in vogal:
            l.append(i+'p'+i)
        else:
            l.append(i)
    return str.join('',l)