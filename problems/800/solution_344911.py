def total(ls,dic):
    o=0
    for e in ls:
        if e in dic:
            o+=dic[e]
    return o