def uppCons(f):
    
    p = str.upper(f)

    for i in range(len(p)):
        if p[i] in 'AEIOU':
            p = p[:i] + str.lower(p[i]) + p[i+1:]
    
    return p