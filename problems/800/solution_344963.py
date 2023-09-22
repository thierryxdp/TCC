def total(ls, produtos):

    r = []

    for p in ls:
        r.append(produtos[p])

    return round(sum(r),2).