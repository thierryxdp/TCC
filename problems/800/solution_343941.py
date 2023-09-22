def total(l, d):
    r = []
    for i in l:
        if i in d:
            r.append(i, (dict.get(d, i)))
        return r